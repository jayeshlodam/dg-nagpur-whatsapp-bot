"""
Utility script for managing DG Nagpur WhatsApp Chatbot
Provides CLI commands for database management, testing, and administration
"""

import sqlite3
import json
from datetime import datetime, timedelta
from database import db
from config import DB_PATH
import sys


def print_header(text):
    """Print formatted header"""
    print("\n" + "="*50)
    print(f"  {text}")
    print("="*50 + "\n")


def print_section(text):
    """Print formatted section"""
    print(f"\n📌 {text}")
    print("-" * 50)


def view_all_leads():
    """Display all leads in a formatted table"""
    print_header("ALL LEADS")
    
    leads = db.get_all_leads()
    
    if not leads:
        print("ℹ️  No leads found yet.\n")
        return
    
    print(f"{'Phone':<15} {'Name':<20} {'Business':<20} {'Category':<10} {'Score':<8}")
    print("-" * 75)
    
    for lead in leads:
        phone = lead['phone_number'][-10:] if lead['phone_number'] else "N/A"
        name = lead['name'][:20] if lead['name'] else "Unknown"[:20]
        business = lead['business_type'][:20] if lead['business_type'] else "N/A"[:20]
        category = lead['lead_category'] or "N/A"
        score = lead['lead_score'] or 0
        
        print(f"{phone:<15} {name:<20} {business:<20} {category:<10} {score:<8}")
    
    print(f"\nTotal Leads: {len(leads)}\n")


def view_lead_details(phone):
    """Display detailed information about a specific lead"""
    lead = db.get_lead(phone)
    
    if not lead:
        print(f"❌ Lead not found: {phone}\n")
        return
    
    print_header(f"LEAD DETAILS: {lead['name'] or 'Unknown'}")
    
    print(f"📱 Phone: {lead['phone_number']}")
    print(f"👤 Name: {lead['name'] or 'Not provided'}")
    print(f"✉️  Email: {lead['email'] or 'Not provided'}")
    print(f"🏢 Business Type: {lead['business_type'] or 'Not provided'}")
    print(f"💰 Budget Range: {lead['budget_range'] or 'Not provided'}")
    print(f"🎯 Goal: {lead['goal'] or 'Not provided'}")
    print(f"📊 Lead Score: {lead['lead_score'] or 0}/100")
    print(f"🏆 Category: {lead['lead_category'] or 'Not categorized'}")
    print(f"📋 Status: {lead['status'] or 'new'}")
    
    if lead['services_interested']:
        try:
            services = json.loads(lead['services_interested'])
            print(f"✅ Services Interested: {', '.join(services)}")
        except:
            pass
    
    if lead['consultation_date']:
        print(f"📅 Consultation Booked: {lead['consultation_date']} at {lead['consultation_time'] or 'TBD'}")
    
    print(f"\n📍 Created: {lead['created_at']}")
    print(f"📍 Updated: {lead['updated_at']}\n")
    
    # Show conversation history
    conversations = db.get_conversation_history(phone, limit=5)
    
    if conversations:
        print_section("Recent Messages (Last 5)")
        for i, conv in enumerate(conversations, 1):
            print(f"\n{i}. [{conv['session_state']}] {conv['created_at']}")
            print(f"   User: {conv['user_message'][:60]}...")
            print(f"   Bot: {conv['bot_response'][:60]}...")


def filter_leads_by_category(category):
    """Show leads in a specific category"""
    print_header(f"{category.upper()} LEADS")
    
    leads = db.get_all_leads(filter_by=category)
    
    if not leads:
        print(f"ℹ️  No {category} leads found.\n")
        return
    
    print(f"Found {len(leads)} {category} leads:\n")
    
    for lead in leads:
        print(f"📱 {lead['phone_number'][-10:]}")
        print(f"   Name: {lead['name'] or 'Unknown'}")
        print(f"   Score: {lead['lead_score'] or 0}/100")
        print(f"   Goal: {lead['goal'] or 'Not specified'}")
        print()


def view_analytics():
    """Display analytics and statistics"""
    print_header("ANALYTICS & STATISTICS")
    
    total_leads = len(db.get_all_leads())
    hot_leads = len(db.get_all_leads(filter_by='hot'))
    warm_leads = len(db.get_all_leads(filter_by='warm'))
    cold_leads = len(db.get_all_leads(filter_by='cold'))
    
    print(f"📊 Total Leads: {total_leads}")
    print(f"🟢 Hot Leads: {hot_leads} ({int(hot_leads/total_leads*100) if total_leads else 0}%)")
    print(f"🟡 Warm Leads: {warm_leads} ({int(warm_leads/total_leads*100) if total_leads else 0}%)")
    print(f"🔴 Cold Leads: {cold_leads} ({int(cold_leads/total_leads*100) if total_leads else 0}%)")
    
    # Message metrics
    messages_received = len(db.get_analytics("message_received", days=30))
    messages_sent = len(db.get_analytics("message_sent", days=30))
    
    print(f"\n💬 Messages (Last 30 days)")
    print(f"   Received: {messages_received}")
    print(f"   Sent: {messages_sent}")
    
    # Service interests
    leads = db.get_all_leads()
    service_counts = {}
    
    for lead in leads:
        if lead['services_interested']:
            try:
                services = json.loads(lead['services_interested'])
                for service in services:
                    service_counts[service] = service_counts.get(service, 0) + 1
            except:
                pass
    
    if service_counts:
        print(f"\n🎯 Top Services Interested:")
        for service, count in sorted(service_counts.items(), key=lambda x: x[1], reverse=True):
            print(f"   {service}: {count} leads")
    
    print()


def view_bookings(date=None):
    """Display consultation bookings"""
    print_header(f"CONSULTATION BOOKINGS{f' - {date}' if date else ''}")
    
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")
    
    bookings = db.get_bookings_by_date(date)
    
    if not bookings:
        print(f"ℹ️  No bookings for {date}\n")
        return
    
    print(f"Bookings for {date}:\n")
    
    for booking in bookings:
        print(f"⏰ {booking['consultation_time']}")
        print(f"   Name: {booking['name']}")
        print(f"   Phone: {booking['phone_number'][-10:]}")
        print(f"   Email: {booking['email']}")
        print(f"   Status: {booking['status']}")
        print()


def update_lead_status(phone, status):
    """Update lead status"""
    db.update_lead(phone, status=status)
    print(f"✅ Lead {phone} status updated to: {status}\n")


def export_leads_csv():
    """Export leads to CSV file"""
    import csv
    
    leads = db.get_all_leads()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"leads_export_{timestamp}.csv"
    
    if not leads:
        print("❌ No leads to export\n")
        return
    
    try:
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['phone_number', 'name', 'email', 'business_type', 'budget_range', 
                         'goal', 'lead_score', 'lead_category', 'status', 'created_at']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for lead in leads:
                writer.writerow({k: lead[k] for k in fieldnames})
        
        print(f"✅ Exported {len(leads)} leads to {filename}\n")
    except Exception as e:
        print(f"❌ Error exporting: {e}\n")


def backup_database():
    """Create database backup"""
    import shutil
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"dg_nagpur_leads_backup_{timestamp}.db"
    
    try:
        shutil.copy(DB_PATH, backup_name)
        print(f"✅ Database backed up to: {backup_name}\n")
    except Exception as e:
        print(f"❌ Backup failed: {e}\n")


def reset_database():
    """Reset database (WARNING: Destructive)"""
    confirm = input("⚠️  WARNING: This will delete all data. Continue? (yes/no): ").lower()
    
    if confirm != "yes":
        print("❌ Cancelled\n")
        return
    
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        cursor.execute("DELETE FROM leads")
        cursor.execute("DELETE FROM conversations")
        cursor.execute("DELETE FROM bookings")
        cursor.execute("DELETE FROM analytics")
        
        conn.commit()
        conn.close()
        
        print("✅ Database reset successfully\n")
    except Exception as e:
        print(f"❌ Reset failed: {e}\n")


def show_help():
    """Display help information"""
    print_header("COMMAND HELP")
    
    help_text = """
USAGE: python utils.py [command] [arguments]

COMMANDS:
  views (v)
    list              - Show all leads
    lead <phone>      - Show detailed lead info
    hot               - Show all hot leads
    warm              - Show all warm leads
    cold              - Show all cold leads
    analytics         - Show analytics and statistics
    bookings [date]   - Show bookings (format: YYYY-MM-DD)

  manage (m)
    status <phone> <status>     - Update lead status
    backup            - Backup database
    export            - Export leads to CSV
    reset             - Reset all data (WARNING!)

  info
    help (-h, --help) - Show this help message
    about             - Show about information

EXAMPLES:
  python utils.py list
  python utils.py lead +919876543210
  python utils.py hot
  python utils.py status +919876543210 contacted
  python utils.py backup
  python utils.py export

"""
    print(help_text)


def show_about():
    """Show about information"""
    print_header("ABOUT DG NAGPUR WHATSAPP CHATBOT")
    
    about_text = """
A professional WhatsApp chatbot for digital marketing agency - Dg Nagpur

Key Features:
  ✅ Lead generation and qualification
  ✅ Service information and pricing
  ✅ Consultation booking system
  ✅ Advanced lead scoring
  ✅ Analytics and reporting
  ✅ WhatsApp Business API integration

Location: Nagpur, India
Services: Social Media, Meta/Google Ads, Web Dev, SEO, Branding, Lead Gen, Content

For support:
  📧 Email: info@dgnagpur.com
  🌐 Website: www.dgnagpur.com

Version: 1.0.0
"""
    print(about_text)


def main():
    """Main CLI interface"""
    
    if len(sys.argv) < 2:
        print_header("DG NAGPUR WHATSAPP CHATBOT - ADMIN UTILITY")
        print("Use: python utils.py help\n")
        print("Quick commands:")
        print("  python utils.py list     - Show all leads")
        print("  python utils.py analytics  - Show statistics")
        print("  python utils.py help     - Show all commands\n")
        return
    
    command = sys.argv[1].lower()
    
    if command in ["-h", "--help", "help"]:
        show_help()
    
    elif command == "about":
        show_about()
    
    elif command in ["v", "view", "views"]:
        if len(sys.argv) > 2:
            subcommand = sys.argv[2].lower()
            
            if subcommand == "list":
                view_all_leads()
            elif subcommand == "lead":
                if len(sys.argv) > 3:
                    view_lead_details(sys.argv[3])
                else:
                    print("❌ Please provide phone number\n")
            elif subcommand in ["hot", "warm", "cold"]:
                filter_leads_by_category(subcommand)
            elif subcommand == "analytics":
                view_analytics()
            elif subcommand == "bookings":
                date = sys.argv[3] if len(sys.argv) > 3 else None
                view_bookings(date)
            else:
                print(f"❌ Unknown view command: {subcommand}\n")
        else:
            view_all_leads()
    
    elif command in ["m", "manage"]:
        if len(sys.argv) > 2:
            subcommand = sys.argv[2].lower()
            
            if subcommand == "status":
                if len(sys.argv) > 4:
                    update_lead_status(sys.argv[3], sys.argv[4])
                else:
                    print("❌ Usage: python utils.py manage status <phone> <status>\n")
            elif subcommand == "backup":
                backup_database()
            elif subcommand == "export":
                export_leads_csv()
            elif subcommand == "reset":
                reset_database()
            else:
                print(f"❌ Unknown manage command: {subcommand}\n")
        else:
            print("❌ Please specify a manage command\n")
    
    else:
        print(f"❌ Unknown command: {command}")
        print("Use 'python utils.py help' for available commands\n")


if __name__ == "__main__":
    main()

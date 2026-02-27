"""
Test/Sandbox Script for DG Nagpur WhatsApp Chatbot
Simulate conversations without needing WhatsApp for testing
"""

from flows import ConversationFlow
from database import db
from config import AGENCY_PHONE, AGENCY_EMAIL, AGENCY_WEBSITE, AGENCY_LOCATION
from messages import CLOSING_MESSAGE
import sys
from datetime import datetime


class ChatbotSimulator:
    """Simulate chatbot conversations for testing"""
    
    def __init__(self, phone_number="+919999999999"):
        self.phone_number = phone_number
        self.conversation_count = 0
    
    def send_message(self, user_input):
        """Send a message and get response"""
        flow = ConversationFlow(self.phone_number)
        response, state = flow.process_message(user_input)
        self.conversation_count += 1
        return response, state
    
    def run_conversation(self, messages):
        """Run a predefined conversation"""
        print("\n" + "="*60)
        print(f"CHATBOT TEST - Conversation with {self.phone_number}")
        print("="*60 + "\n")
        
        for i, message in enumerate(messages, 1):
            print(f"📱 User [{i}]: {message}")
            response, state = self.send_message(message)
            print(f"\n🤖 Bot [{state}]:")
            print(response)
            print("\n" + "-"*60 + "\n")
        
        print(f"✅ Conversation complete ({self.conversation_count} messages)")
        print("="*60 + "\n")


def test_complete_flow():
    """Test complete lead qualification and booking flow"""
    
    test_messages = [
        "Hi",
        "1",  # Services
        "2",  # Meta Ads
        "Yes",  # Interested
        "2",  # Business type - Ecommerce
        "2",  # Budget - ₹5,000-15,000
        "2",  # Goal - Increase sales
        "Amit Sharma",  # Name
        "amit.sharma@business.com",  # Email
        "Yes",  # Consultation booking
        "15/03/2026",  # Date
        "2:00 PM",  # Time
    ]
    
    sim = ChatbotSimulator("+919876543210")
    sim.run_conversation(test_messages)
    
    # Show lead data
    lead = db.get_lead("+919876543210")
    print("\n" + "="*60)
    print("LEAD DATA CAPTURED:")
    print("="*60)
    if lead:
        print(f"Name: {lead['name']}")
        print(f"Phone: {lead['phone_number']}")
        print(f"Email: {lead['email']}")
        print(f"Business: {lead['business_type']}")
        print(f"Budget: {lead['budget_range']}")
        print(f"Goal: {lead['goal']}")
        print(f"Lead Score: {lead['lead_score']}/100")
        print(f"Category: {lead['lead_category']}")
        print(f"Consultation: {lead['consultation_date']} at {lead['consultation_time']}")
    print("="*60 + "\n")


def test_service_enquiry():
    """Test service interest flow"""
    print("\n" + "="*60)
    print("TEST: Service Enquiry Flow")
    print("="*60 + "\n")
    
    test_messages = [
        "Hello",
        "Services",
        "5",  # SEO
        "Tell me more about SEO",
        "Are you interested in implementing SEO?",
    ]
    
    sim = ChatbotSimulator("+919123456789")
    sim.run_conversation(test_messages)


def test_pricing_enquiry():
    """Test pricing enquiry"""
    print("\n" + "="*60)
    print("TEST: Pricing Enquiry Flow")
    print("="*60 + "\n")
    
    test_messages = [
        "Hi guys",
        "2",  # Pricing
        "Which plan do you recommend?",
        "Menu",
        "Back",
    ]
    
    sim = ChatbotSimulator("+919111111111")
    sim.run_conversation(test_messages)


def test_portfolio_view():
    """Test portfolio viewing"""
    print("\n" + "="*60)
    print("TEST: Portfolio View Flow")
    print("="*60 + "\n")
    
    test_messages = [
        "Hello",
        "4",  # Portfolio
        "Can you show me more case studies?",
        "Menu",
    ]
    
    sim = ChatbotSimulator("+919222222222")
    sim.run_conversation(test_messages)


def test_expert_connect():
    """Test expert connection"""
    print("\n" + "="*60)
    print("TEST: Expert Connect Flow")
    print("="*60 + "\n")
    
    test_messages = [
        "Hello",
        "5",  # Talk to expert
        "I want to discuss my project",
        "Menu",
    ]
    
    sim = ChatbotSimulator("+919333333333")
    sim.run_conversation(test_messages)


def test_fallback_handling():
    """Test fallback message handling"""
    print("\n" + "="*60)
    print("TEST: Fallback Handling (Invalid inputs)")
    print("="*60 + "\n")
    
    test_messages = [
        "Hello",
        "xyz123",  # Invalid input
        "123456",  # Invalid input
        "@#$%",    # Invalid input
        "Menu",
        "1",  # Valid input after fallback
    ]
    
    sim = ChatbotSimulator("+919444444444")
    sim.run_conversation(test_messages)


def test_quick_consultation_book():
    """Test quick consultation booking"""
    print("\n" + "="*60)
    print("TEST: Quick Consultation Booking")
    print("="*60 + "\n")
    
    test_messages = [
        "Hi",
        "3",  # Book Consultation
        "1",  # Real Estate
        "3",  # Budget 15k-30k
        "1",  # Generate leads
        "Rajesh Patel",  # Name
        "rajesh@realestate.com",  # Email
        "Yes",  # Book consultation
        "20/03/2026",  # Date
        "10:00 AM",  # Time
    ]
    
    sim = ChatbotSimulator("+919555555555")
    sim.run_conversation(test_messages)


def run_interactive_mode():
    """Run interactive chatbot test mode"""
    print("\n" + "="*60)
    print("🤖 INTERACTIVE CHATBOT TEST MODE")
    print("="*60)
    print("\nChat with the chatbot in real-time (simulated)")
    print("Type 'exit' to quit, 'lead' to see current lead data\n")
    
    phone = input("Enter phone number to test with (default: +919999999999): ").strip()
    if not phone:
        phone = "+919999999999"
    
    print(f"\nStarting conversation with {phone}")
    print("-"*60 + "\n")
    
    sim = ChatbotSimulator(phone)
    message_count = 0
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if not user_input:
                continue
            
            if user_input.lower() == "exit":
                print("\nGoodbye! 👋")
                break
            
            if user_input.lower() == "lead":
                lead = db.get_lead(phone)
                if lead:
                    print("\n--- Current Lead Data ---")
                    print(f"Name: {lead['name']}")
                    print(f"Email: {lead['email']}")
                    print(f"Business: {lead['business_type']}")
                    print(f"Budget: {lead['budget_range']}")
                    print(f"Goal: {lead['goal']}")
                    print(f"Score: {lead['lead_score']}/100")
                    print(f"Category: {lead['lead_category']}")
                    print("------------------------\n")
                else:
                    print("No lead data yet.\n")
                continue
            
            response, state = sim.send_message(user_input)
            print(f"\nBot ({state}):\n{response}\n")
            message_count += 1
        
        except KeyboardInterrupt:
            print("\n\nChat interrupted.")
            break
        except Exception as e:
            print(f"Error: {e}\n")


def show_menu():
    """Show test menu"""
    print("\n" + "="*60)
    print("🧪 DG NAGPUR CHATBOT - TEST SUITE")
    print("="*60 + "\n")
    
    print("Available Tests:\n")
    print("1. Complete Lead Qualification Flow")
    print("2. Service Enquiry Flow")
    print("3. Pricing Enquiry Flow")
    print("4. Portfolio View Flow")
    print("5. Expert Connect Flow")
    print("6. Fallback Handling (Invalid Inputs)")
    print("7. Quick Consultation Booking")
    print("8. Interactive Chat Mode")
    print("0. Exit")
    print("\n" + "="*60 + "\n")


def main():
    """Main test interface"""
    
    if len(sys.argv) > 1:
        test_num = sys.argv[1]
    else:
        while True:
            show_menu()
            
            try:
                test_num = input("Select test (0-8): ").strip()
            except KeyboardInterrupt:
                print("\n\nTests cancelled.")
                return
            
            if not test_num.isdigit():
                print("Invalid input. Please enter a number.\n")
                continue
            
            test_num = int(test_num)
            break
    
    tests = {
        "0": lambda: None,
        "1": test_complete_flow,
        "2": test_service_enquiry,
        "3": test_pricing_enquiry,
        "4": test_portfolio_view,
        "5": test_expert_connect,
        "6": test_fallback_handling,
        "7": test_quick_consultation_book,
        "8": run_interactive_mode,
    }
    
    if str(test_num) in tests:
        test_func = tests[str(test_num)]
        if test_func:
            try:
                test_func()
            except Exception as e:
                print(f"\n❌ Test error: {e}")
                import traceback
                traceback.print_exc()
        else:
            print("Exiting tests.")
    else:
        print(f"Invalid test number: {test_num}\n")


if __name__ == "__main__":
    main()

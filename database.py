"""
Database Module for DG Nagpur WhatsApp Chatbot
Handles lead storage, conversation history, and data persistence
"""

import sqlite3
import json
from datetime import datetime
from config import DB_PATH

class Database:
    def __init__(self, db_path=DB_PATH):
        self.db_path = db_path
        self.init_database()
    
    def get_connection(self):
        """Create and return database connection"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn
    
    def init_database(self):
        """Initialize database tables"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # Leads table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS leads (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                phone_number TEXT UNIQUE NOT NULL,
                name TEXT,
                email TEXT,
                business_type TEXT,
                budget_range TEXT,
                goal TEXT,
                lead_score INTEGER,
                lead_category TEXT,
                services_interested TEXT,
                consultation_date TEXT,
                consultation_time TEXT,
                status TEXT DEFAULT 'new',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Conversation history table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS conversations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                phone_number TEXT NOT NULL,
                user_message TEXT,
                bot_response TEXT,
                session_state TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (phone_number) REFERENCES leads(phone_number)
            )
        ''')
        
        # Bookings table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS bookings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                lead_id INTEGER,
                consultation_date TEXT NOT NULL,
                consultation_time TEXT NOT NULL,
                duration INTEGER DEFAULT 30,
                status TEXT DEFAULT 'pending',
                meeting_link TEXT,
                notes TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (lead_id) REFERENCES leads(id)
            )
        ''')
        
        # Analytics table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS analytics (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                metric_type TEXT,
                value INTEGER,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        conn.commit()
        conn.close()
    
    # LEAD MANAGEMENT
    
    def add_lead(self, phone_number, name=None, email=None):
        """Add or update lead"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute('''
                INSERT OR REPLACE INTO leads (phone_number, name, email, updated_at)
                VALUES (?, ?, ?, CURRENT_TIMESTAMP)
            ''', (phone_number, name, email))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error adding lead: {e}")
            return False
        finally:
            conn.close()
    
    def get_lead(self, phone_number):
        """Get lead details by phone number"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM leads WHERE phone_number = ?', (phone_number,))
        lead = cursor.fetchone()
        conn.close()
        
        return dict(lead) if lead else None
    
    def update_lead(self, phone_number, **kwargs):
        """Update lead information"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        fields = []
        values = []
        
        for key, value in kwargs.items():
            if key in ['name', 'email', 'business_type', 'budget_range', 'goal', 
                      'lead_score', 'lead_category', 'services_interested', 
                      'consultation_date', 'consultation_time', 'status']:
                fields.append(f"{key} = ?")
                values.append(value)
        
        if not fields:
            conn.close()
            return False
        
        fields.append("updated_at = CURRENT_TIMESTAMP")
        values.append(phone_number)
        
        query = f"UPDATE leads SET {', '.join(fields)} WHERE phone_number = ?"
        
        try:
            cursor.execute(query, values)
            conn.commit()
            return True
        except Exception as e:
            print(f"Error updating lead: {e}")
            return False
        finally:
            conn.close()
    
    def calculate_lead_score(self, phone_number):
        """Calculate lead score based on interactions and details"""
        lead = self.get_lead(phone_number)
        if not lead:
            return 0
        
        score = 0
        
        # Score based on information provided
        if lead['name']:
            score += 10
        if lead['email']:
            score += 10
        if lead['business_type']:
            score += 15
        if lead['budget_range']:
            score += 25
        if lead['goal']:
            score += 15
        
        # Score based on engagement
        conversations = self.get_conversation_count(phone_number)
        score += min(conversations * 5, 15)  # Max 15 points for engagement
        
        # Score based on service interest
        if lead['services_interested']:
            services = json.loads(lead['services_interested']) if isinstance(lead['services_interested'], str) else []
            score += len(services) * 5
        
        # Validate score range
        score = min(score, 100)
        
        # Update in database
        self.update_lead(phone_number, lead_score=score)
        
        # Categorize lead
        category = "cold"
        if score >= 80:
            category = "hot"
        elif score >= 50:
            category = "warm"
        
        self.update_lead(phone_number, lead_category=category)
        
        return score
    
    def get_all_leads(self, filter_by=None):
        """Get all leads, optionally filtered by status or category"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        if filter_by:
            query = "SELECT * FROM leads WHERE lead_category = ? ORDER BY updated_at DESC"
            cursor.execute(query, (filter_by,))
        else:
            cursor.execute("SELECT * FROM leads ORDER BY updated_at DESC")
        
        leads = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return leads
    
    # CONVERSATION MANAGEMENT
    
    def add_conversation(self, phone_number, user_message, bot_response, state):
        """Log conversation"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute('''
                INSERT INTO conversations (phone_number, user_message, bot_response, session_state)
                VALUES (?, ?, ?, ?)
            ''', (phone_number, user_message, bot_response, state))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error adding conversation: {e}")
            return False
        finally:
            conn.close()
    
    def get_conversation_history(self, phone_number, limit=10):
        """Get recent conversation history"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT * FROM conversations 
            WHERE phone_number = ? 
            ORDER BY created_at DESC 
            LIMIT ?
        ''', (phone_number, limit))
        
        conversations = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return list(reversed(conversations))  # Return in chronological order
    
    def get_conversation_count(self, phone_number):
        """Count total conversations with a user"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT COUNT(*) FROM conversations WHERE phone_number = ?', (phone_number,))
        count = cursor.fetchone()[0]
        conn.close()
        return count
    
    # BOOKING MANAGEMENT
    
    def add_booking(self, lead_id, date, time, meeting_link=None, notes=None):
        """Create consultation booking"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute('''
                INSERT INTO bookings (lead_id, consultation_date, consultation_time, meeting_link, notes)
                VALUES (?, ?, ?, ?, ?)
            ''', (lead_id, date, time, meeting_link, notes))
            conn.commit()
            booking_id = cursor.lastrowid
            return booking_id
        except Exception as e:
            print(f"Error adding booking: {e}")
            return None
        finally:
            conn.close()
    
    def get_booking(self, booking_id):
        """Get booking details"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM bookings WHERE id = ?', (booking_id,))
        booking = cursor.fetchone()
        conn.close()
        
        return dict(booking) if booking else None
    
    def get_bookings_by_date(self, date):
        """Get all bookings for a specific date"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT b.*, l.name, l.phone_number, l.email 
            FROM bookings b
            JOIN leads l ON b.lead_id = l.id
            WHERE b.consultation_date = ?
            ORDER BY b.consultation_time
        ''', (date,))
        
        bookings = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return bookings
    
    # ANALYTICS
    
    def track_metric(self, metric_type, value=1):
        """Track analytics metrics"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute('''
                INSERT INTO analytics (metric_type, value)
                VALUES (?, ?)
            ''', (metric_type, value))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error tracking metric: {e}")
            return False
        finally:
            conn.close()
    
    def get_analytics(self, metric_type, days=30):
        """Get analytics for a specific metric"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT COUNT(*) as total, DATE(timestamp) as date
            FROM analytics
            WHERE metric_type = ? 
            AND timestamp >= datetime('now', '-' || ? || ' days')
            GROUP BY DATE(timestamp)
        ''', (metric_type, days))
        
        analytics = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return analytics


# Initialize database instance
db = Database()

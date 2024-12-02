from database.db_config import DatabaseConfig
from datetime import datetime

class RMARepository:
    def __init__(self):
        self.db = DatabaseConfig()
    
    def create_rma(self, data: dict) -> tuple[bool, int, str]:
        """Create a new RMA entry"""
        try:
            with self.db.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO RMA (
                        rma_number, company_id, product_name,
                        issue_description, status, priority
                    ) VALUES (?, ?, ?, ?, ?, ?)
                """, (
                    data['rma_number'],
                    data['company_id'],
                    data['product_name'],
                    data['issue_description'],
                    data['status'],
                    data['priority']
                ))
                conn.commit()
                return True, cursor.lastrowid, "RMA created successfully"
        except Exception as e:
            return False, 0, f"Error creating RMA: {str(e)}"
    
    def get_rma_list(self, status_filter: str = None) -> list[dict]:
        """Get list of RMAs with optional status filter"""
        try:
            with self.db.get_connection() as conn:
                cursor = conn.cursor()
                
                query = """
                    SELECT r.*, c.company_name
                    FROM RMA r
                    JOIN CompanyContacts c ON r.company_id = c.company_id
                """
                
                params = []
                if status_filter and status_filter.lower() != 'all':
                    query += " WHERE r.status = ?"
                    params.append(status_filter)
                
                query += " ORDER BY r.date_created DESC"
                
                cursor.execute(query, params)
                columns = [col[0] for col in cursor.description]
                return [dict(zip(columns, row)) for row in cursor.fetchall()]
        except Exception as e:
            print(f"Error fetching RMAs: {str(e)}")
            return []
    
    def get_rma_by_id(self, rma_id: int) -> dict:
        """Get RMA details by ID"""
        try:
            with self.db.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT r.*, c.company_name
                    FROM RMA r
                    JOIN CompanyContacts c ON r.company_id = c.company_id
                    WHERE r.rma_id = ?
                """, (rma_id,))
                
                columns = [col[0] for col in cursor.description]
                row = cursor.fetchone()
                return dict(zip(columns, row)) if row else None
        except Exception as e:
            print(f"Error fetching RMA: {str(e)}")
            return None
    
    def update_rma(self, rma_id: int, data: dict) -> tuple[bool, str]:
        """Update an existing RMA"""
        try:
            with self.db.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    UPDATE RMA
                    SET product_name = ?,
                        issue_description = ?,
                        status = ?,
                        priority = ?,
                        last_updated = CURRENT_DATE
                    WHERE rma_id = ?
                """, (
                    data['product_name'],
                    data['issue_description'],
                    data['status'],
                    data['priority'],
                    rma_id
                ))
                conn.commit()
                return True, "RMA updated successfully"
        except Exception as e:
            return False, f"Error updating RMA: {str(e)}"}
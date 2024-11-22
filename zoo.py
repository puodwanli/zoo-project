class Zoo:
    def get_ticket_price(self, age):
        # Validate age: Ensure age is a non-negative integer
        if not isinstance(age, int) or age < 0:
            return "Invalid age"

        # Ticket pricing logic
        if age <= 12:  
            return 50
        elif 13 <= age <= 20:  
            return 100
        elif 21 <= age <= 60:  
            return 150
        elif age > 60:  
            return 100
        return "Invalid age" 

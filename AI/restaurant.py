# Restaurant Recommendation Expert System


# Knowledge Base (Facts)
restaurants = [
    # Indian Cuisine
    {"name": "Spice Hub", "cuisine": "Indian", "price": "medium", "ambiance": "family", "rating": 4.5},
    {"name": "Tandoori Treats", "cuisine": "Indian", "price": "high", "ambiance": "romantic", "rating": 4.7},
    {"name": "Curry Corner", "cuisine": "Indian", "price": "low", "ambiance": "casual", "rating": 4.3},
    {"name": "Royal Thali", "cuisine": "Indian", "price": "medium", "ambiance": "peaceful", "rating": 4.4},

    # Italian Cuisine
    {"name": "Pasta Palace", "cuisine": "Italian", "price": "high", "ambiance": "romantic", "rating": 4.7},
    {"name": "Mama Mia Café", "cuisine": "Italian", "price": "medium", "ambiance": "family", "rating": 4.5},
    {"name": "Budget Bites Italiano", "cuisine": "Italian", "price": "low", "ambiance": "casual", "rating": 4.2},

    # Japanese Cuisine
    {"name": "Sushi World", "cuisine": "Japanese", "price": "high", "ambiance": "quiet", "rating": 4.8},
    {"name": "Tokyo Taste", "cuisine": "Japanese", "price": "medium", "ambiance": "romantic", "rating": 4.6},
    {"name": "Noodle House", "cuisine": "Japanese", "price": "low", "ambiance": "casual", "rating": 4.3},

    # Fast Food
    {"name": "Burger Point", "cuisine": "Fast Food", "price": "low", "ambiance": "casual", "rating": 4.2},
    {"name": "Snack Station", "cuisine": "Fast Food", "price": "medium", "ambiance": "family", "rating": 4.3},
    {"name": "Drive-Thru Diner", "cuisine": "Fast Food", "price": "high", "ambiance": "quiet", "rating": 4.5},

    # Vegan Cuisine
    {"name": "Green Leaf", "cuisine": "Vegan", "price": "medium", "ambiance": "peaceful", "rating": 4.4},
    # {"name": "Nature’s Bowl", "cuisine": "Vegan", "price": "low", "ambiance": "casual", "rating": 4.3},
    {"name": "Organic Oasis", "cuisine": "Vegan", "price": "high", "ambiance": "romantic", "rating": 4.6},
    {"name": "Healthy Harvest", "cuisine": "Vegan", "price": "medium", "ambiance": "family", "rating": 4.5},
]


# Inference Engine (Rules)
def recommend_restaurants(cuisine_pref, price_pref, ambiance_pref):
    recommendations = []

    for r in restaurants:
        score = 0
        
        # Rule 1: Match cuisine
        if r["cuisine"].lower() == cuisine_pref.lower():
            score += 3
        
        # Rule 2: Match price
        if r["price"].lower() == price_pref.lower():
            score += 2
        
        # Rule 3: Match ambiance
        if r["ambiance"].lower() == ambiance_pref.lower():
            score += 2
        
        # Rule 4: High rating bonus
        if r["rating"] >= 4.5:
            score += 1
        
        # If rule-based score >= 4, it’s a good match
        if score >= 4:
            recommendations.append((r["name"], r["rating"]))
    
    # Sort by rating (descending)
    return sorted(recommendations, key=lambda x: x[1], reverse=True)


# User Interaction (Facts from User)
print("🍽️ Welcome to the Restaurant Recommendation Expert System 🍽️")
print("Please answer a few questions so I can recommend the best restaurant for you!\n")

cuisine = input("What type of cuisine do you prefer? (Indian/Italian/Japanese/Fast Food/Vegan): ")
price = input("What is your preferred price range? (low/medium/high): ")
ambiance = input("What kind of ambiance do you prefer? (family/romantic/quiet/casual/peaceful): ")

# Reasoning & Output
result = recommend_restaurants(cuisine, price, ambiance)

if result:
    print("\n✅ Recommended Restaurants for You:")
    for name, rating in result:
        print(f" - {name} (⭐ {rating})")
else:
    print("\n❌ Sorry, no restaurant matches your preferences exactly.")
    print("Try changing your preferences slightly!")

    
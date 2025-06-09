def get_template(category):
    templates = {
        "electronics": (
            "Introducing {product_name}, featuring {features}. Benefits include {benefits}. "
            "Why choose this? {usp}. Technical Details:\n{specs}"
        ),
        "fashion": (
            "Upgrade your style with {product_name}. Highlights: {features}. Enjoy {benefits}. "
            "What makes it special? {usp}. Specifications:\n{specs}"
        ),
        # Add more categories as needed
    }
    return templates.get(category, templates['electronics'])

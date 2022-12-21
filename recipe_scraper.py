from recipe_scrapers import scrape_me

# give the url as a string, it can be url from any site listed below


def get_basic_info(URL):
    scraper = scrape_me(URL)
    title = scraper.title()
    total_time = scraper.total_time()/60
    output = []
    output.append(title)
    output.append(total_time)
    return output

def get_ingredients(URL):
    scraper = scrape_me(URL)
    ingredients = scraper.ingredients()
    return ingredients

def get_instructions(URL):
    scraper = scrape_me(URL)
    instructions = scraper.instructions_list()
    return instructions

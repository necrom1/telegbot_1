import random
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Обновленный список героев с атрибутами
heroes = [
    {"name": "Abaddon", "attribute": "Strength"},
    {"name": "Alchemist", "attribute": "Strength"},
    {"name": "Ancient Apparition", "attribute": "Intelligence"},
    {"name": "Anti-Mage", "attribute": "Agility"},
    {"name": "Axe", "attribute": "Strength"},
    {"name": "Bane", "attribute": "Intelligence"},
    {"name": "Batrider", "attribute": "Intelligence"},
    {"name": "Beastmaster", "attribute": "Strength"},
    {"name": "Bloodseeker", "attribute": "Agility"},
    {"name": "Bounty Hunter", "attribute": "Agility"},
    {"name": "Brewmaster", "attribute": "Strength"},
    {"name": "Bristleback", "attribute": "Strength"},
    {"name": "Broodmother", "attribute": "Agility"},
    {"name": "Centaur Warrunner", "attribute": "Strength"},
    {"name": "Chaos Knight", "attribute": "Strength"},
    {"name": "Chen", "attribute": "Intelligence"},
    {"name": "Clinkz", "attribute": "Agility"},
    {"name": "Crystal Maiden", "attribute": "Intelligence"},
    {"name": "Dark Seer", "attribute": "Intelligence"},
    {"name": "Dazzle", "attribute": "Intelligence"},
    {"name": "Death Prophet", "attribute": "Intelligence"},
    {"name": "Disruptor", "attribute": "Intelligence"},
    {"name": "Doom", "attribute": "Strength"},
    {"name": "Dragon Knight", "attribute": "Strength"},
    {"name": "Drow Ranger", "attribute": "Agility"},
    {"name": "Earthshaker", "attribute": "Strength"},
    {"name": "Earth Spirit", "attribute": "Strength"},
    {"name": "Elder Titan", "attribute": "Strength"},
    {"name": "Ember Spirit", "attribute": "Agility"},
    {"name": "Enchantress", "attribute": "Intelligence"},
    {"name": "Enigma", "attribute": "Intelligence"},
    {"name": "Faceless Void", "attribute": "Agility"},
    {"name": "Grimstroke", "attribute": "Intelligence"},
    {"name": "Gyrocopter", "attribute": "Agility"},
    {"name": "Huskar", "attribute": "Strength"},
    {"name": "Invoker", "attribute": "Intelligence"},
    {"name": "Io", "attribute": "Strength"},
    {"name": "Jakiro", "attribute": "Intelligence"},
    {"name": "Juggernaut", "attribute": "Agility"},
    {"name": "Keeper of the Light", "attribute": "Intelligence"},
    {"name": "Kunkka", "attribute": "Strength"},
    {"name": "Legion Commander", "attribute": "Strength"},
    {"name": "Leshrac", "attribute": "Intelligence"},
    {"name": "Lich", "attribute": "Intelligence"},
    {"name": "Lifestealer", "attribute": "Strength"},
    {"name": "Lina", "attribute": "Intelligence"},
    {"name": "Lion", "attribute": "Intelligence"},
    {"name": "Lone Druid", "attribute": "Agility"},
    {"name": "Luna", "attribute": "Agility"},
    {"name": "Lycan", "attribute": "Strength"},
    {"name": "Magnus", "attribute": "Strength"},
    {"name": "Mars", "attribute": "Strength"},
    {"name": "Medusa", "attribute": "Agility"},
    {"name": "Meepo", "attribute": "Agility"},
    {"name": "Mirana", "attribute": "Agility"},
    {"name": "Monkey King", "attribute": "Agility"},
    {"name": "Morphling", "attribute": "Agility"},
    {"name": "Naga Siren", "attribute": "Agility"},
    {"name": "Nature's Prophet", "attribute": "Intelligence"},
    {"name": "Necrophos", "attribute": "Intelligence"},
    {"name": "Night Stalker", "attribute": "Strength"},
    {"name": "Nyx Assassin", "attribute": "Agility"},
    {"name": "Ogre Magi", "attribute": "Intelligence"},
    {"name": "Omniknight", "attribute": "Strength"},
    {"name": "Oracle", "attribute": "Intelligence"},
    {"name": "Outworld Destroyer", "attribute": "Intelligence"},
    {"name": "Pangolier", "attribute": "Agility"},
    {"name": "Phantom Assassin", "attribute": "Agility"},
    {"name": "Phantom Lancer", "attribute": "Agility"},
    {"name": "Phoenix", "attribute": "Strength"},
    {"name": "Puck", "attribute": "Intelligence"},
    {"name": "Pudge", "attribute": "Strength"},
    {"name": "Pugna", "attribute": "Intelligence"},
    {"name": "Queen of Pain", "attribute": "Intelligence"},
    {"name": "Razor", "attribute": "Agility"},
    {"name": "Riki", "attribute": "Agility"},
    {"name": "Rubick", "attribute": "Intelligence"},
    {"name": "Sand King", "attribute": "Strength"},
    {"name": "Shadow Demon", "attribute": "Intelligence"},
    {"name": "Shadow Fiend", "attribute": "Agility"},
    {"name": "Shadow Shaman", "attribute": "Intelligence"},
    {"name": "Silencer", "attribute": "Intelligence"},
    {"name": "Skywrath Mage", "attribute": "Intelligence"},
    {"name": "Slardar", "attribute": "Strength"},
    {"name": "Slark", "attribute": "Agility"},
    {"name": "Snapfire", "attribute": "Strength"},
    {"name": "Sniper", "attribute": "Agility"},
    {"name": "Spectre", "attribute": "Agility"},
    {"name": "Spirit Breaker", "attribute": "Strength"},
    {"name": "Storm Spirit", "attribute": "Intelligence"},
    {"name": "Sven", "attribute": "Strength"},
    {"name": "Techies", "attribute": "Intelligence"},
    {"name": "Templar Assassin", "attribute": "Agility"},
    {"name": "Terrorblade", "attribute": "Agility"},
    {"name": "Tidehunter", "attribute": "Strength"},
    {"name": "Timbersaw", "attribute": "Strength"},
    {"name": "Tinker", "attribute": "Intelligence"},
    {"name": "Tiny", "attribute": "Strength"},
    {"name": "Treant Protector", "attribute": "Strength"},
    {"name": "Troll Warlord", "attribute": "Agility"},
    {"name": "Tusk", "attribute": "Strength"},
    {"name": "Underlord", "attribute": "Strength"},
    {"name": "Undying", "attribute": "Strength"},
    {"name": "Ursa", "attribute": "Agility"},
    {"name": "Vengeful Spirit", "attribute": "Agility"},
    {"name": "Venomancer", "attribute": "Agility"},
    {"name": "Viper", "attribute": "Agility"},
    {"name": "Visage", "attribute": "Intelligence"},
    {"name": "Void Spirit", "attribute": "Agility"},
    {"name": "Warlock", "attribute": "Intelligence"},
    {"name": "Weaver", "attribute": "Agility"},
    {"name": "Windranger", "attribute": "Intelligence"},
    {"name": "Winter Wyvern", "attribute": "Intelligence"},
    {"name": "Witch Doctor", "attribute": "Intelligence"},
    {"name": "Wraith King", "attribute": "Strength"},
    {"name": "Zeus", "attribute": "Intelligence"}
]

# Список предметов для сборки
items = [
    "Black King Bar",
    "Blink Dagger",
    "Force Staff",
    "Sange and Yasha",
    "Heart of Tarrasque",
    "Butterfly",
    "Divine Rapier",
    "Aghanim's Scepter",
    "Manta Style",
    "Assault Cuirass",
    "Crimson Guard",
    "Pipe of Insight",
    "Ethereal Blade",
    "Radiance",
    "Monkey King Bar"
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    help_text = (
        "Привет! Я бот для Dota 2.\n"
        "Команды:\n"
        "/start - это меню\n"
        "/randomhero [атрибут] - случайный герой (можно указать Strength/Agility/Intelligence)\n"
        "/randomitem - случайный предмет для сборки"
    )
    await update.message.reply_text(help_text)

async def random_hero(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        attribute = context.args[0].capitalize() if context.args else None
        valid_attributes = ["Strength", "Agility", "Intelligence"]

        if attribute and attribute not in valid_attributes:
            raise ValueError

        filtered_heroes = [h for h in heroes if h["attribute"] == attribute] if attribute else heroes
        hero = random.choice(filtered_heroes)
        item = random.choice(items)

        response = (
            f"Герой ({hero['attribute']}): {hero['name']}\n"
            f"Рекомендуемый предмет: {item}\n"
            f"Стратегия: {get_strategy_advice(hero['attribute'])}"
        )

    except (IndexError, ValueError):
        response = "Используйте: /randomhero [Strength/Agility/Intelligence]"
    except Exception as e:
        response = f"Ошибка: {str(e)}"

    await update.message.reply_text(response)

async def random_item(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    item = random.choice(items)
    advice = get_item_advice(item)
    await update.message.reply_text(f"Случайный предмет: {item}\n{advice}")

def get_strategy_advice(attribute: str) -> str:
    advice = {
        "Strength": "Фокусируйтесь на танковании и инициации в боях!",
        "Agility": "Собирайте предметы на атаку и скорость атаки!",
        "Intelligence": "Используйте комбинации способностей и контролируйте карту!"
    }
    return advice.get(attribute, "Адаптируйте стратегию под ситуацию!")

def get_item_advice(item: str) -> str:
    item_advice = {
        "Black King Bar": "Обязателен против магического урона!",
        "Blink Dagger": "Идеален для инициации боя!",
        "Force Staff": "Спасайте союзников или преследуйте врагов!",
        "Divine Rapier": "Очень рискованный, но мощный выбор!",
        "Radiance": "Отлично подходит для фарма и давления!"
    }
    return item_advice.get(item, "Эффективно используйте этот предмет в разных ситуациях!")

def main() -> None:
    application = Application.builder().token("7490444852:AAFoMTJlCtlAYKeT20HMS1Ibb-xvm1ggSpQ").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("randomhero", random_hero))
    application.add_handler(CommandHandler("randomitem", random_item))

    application.run_polling()

if __name__ == '__main__':
    main()

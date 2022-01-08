import random

R_EATING = "aku gasuka makan karna aku BOT :( "
R_ADVICE = "Kalau aku jadi kamu aku akan banyak belajar hal baru "


def unknown():
    response = ["Apa kabar? ",
                "Hari akan cerah",
                "Bawa payung ya,sepertinya akan hujan",
                "makan apa ya?",
                "Aku ga ngerti nih",
                "...",
                "capek ga?",
                "Maksud nya apa ?"][
        random.randrange(8)]
    return response

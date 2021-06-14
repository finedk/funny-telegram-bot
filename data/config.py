from environs import Env

env = Env()
env.read_env()

api_key = env.str("api_key")
admin = env.int("admin") # ID администратора - кого нужно уведомлять о состоянии бота
who_need_notif = env.list("who_need_notif")
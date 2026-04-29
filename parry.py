import curses
import time
import random

def game(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)

    player_hp = 100
    enemy_hp = 100

    log = ""
    attack_active = False
    attack_type = None
    attack_time = 0

    parry_window = 0.8
    damage = 15

    while True:
        stdscr.clear()
        now = time.time()

        # 🎲 generar ataque enemigo
        if not attack_active and random.random() < 0.02:
            attack_active = True
            attack_time = now

            # 🔥 50% rojo (parry), 50% verde (dodge)
            attack_type = random.choice(["red", "green"])

            if attack_type == "red":
                log = "🔴 Enemy attacks! PARRY!"
            else:
                log = "🟢 Green attack! DON'T parry (auto dodge)"

        key = stdscr.getch()

        if key != -1:
            char = chr(key)

            if char == "p" and attack_active:

                # 🔴 ataque parry
                if attack_type == "red":
                    if now - attack_time <= parry_window:
                        log = "🛡️ PERFECT PARRY!"
                        enemy_hp -= 10
                    else:
                        log = "❌ Too slow!"
                        player_hp -= damage

                # 🟢 ataque verde (castiga parry)
                elif attack_type == "green":
                    log = "💥 WRONG INPUT!"
                    player_hp -= damage

                attack_active = False

        # 🟢 dodge automático si es verde y no hiciste nada
        if attack_active and attack_type == "green":
            if now - attack_time > parry_window:
                log = "🟢 Auto dodge success!"
                attack_active = False

        # 🔴 fallo de parry si no reaccionas
        if attack_active and attack_type == "red":
            if now - attack_time > parry_window:
                log = "💥 HIT!"
                player_hp -= damage
                attack_active = False

        # UI
        stdscr.addstr(1, 1, f"HP: {player_hp}")
        stdscr.addstr(2, 1, f"Enemy HP: {enemy_hp}")
        stdscr.addstr(4, 1, log)
        stdscr.addstr(6, 1, "P = parry (solo rojo)")

        stdscr.refresh()
        time.sleep(0.05)

curses.wrapper(game)

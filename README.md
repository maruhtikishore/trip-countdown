# Sri Lanka Trip Countdown 🌴

Posts countdown messages to the **Sri Lanka** WhatsApp group automatically, every morning at 9:00 AM, until the trip.

- **Trip:** 25 Dec 2026 (flight 9:50 AM) → **Return:** 1 Jan 2027 (flight 7:25 AM)
- **More than 20 days left:** posts only when the days left are divisible by 10 (60, 50, 40, 30)
- **20 days or fewer:** posts every day, with more excited messages
- **Trip day (0 days):** stops posting automatically

## How it works

```
Laptop (one time)                    iPhone (every day, automatic)
─────────────────                    ─────────────────────────────
config.json + messages.py            9:00 AM automation runs "Trip Counter"
        │                                    │
generate_schedule.py                 Looks up today's date in the list
        │                                    │
countdown_schedule.json  ──pasted──▶  Message for today?  ── no ──▶ does nothing
                                             │ yes
                                     Sends it to Green API ──▶ posted in the group
```

The laptop only prepares the message list. After that, the iPhone does everything, so the laptop doesn't need to be on.

## Files

| File | Purpose |
|---|---|
| `config.json` | Trip date, flight times, destination, emoji, group link |
| `messages.py` | All message styles (regular, final stretch, and fixed milestone messages) |
| `generate_schedule.py` | Builds `countdown_schedule.json` from the config and messages |
| `countdown_schedule.json` | The final list of date → message (24 posts). This is what's pasted into the iPhone |
| `greenapi.py` | Laptop tool to check, test, or send through Green API |
| `greenapi_secrets.json` | 🔒 Green API login and group ID. **Never share this file** |

## Laptop commands

Run these from this folder (Python 3, no installs needed):

| Command | What it does |
|---|---|
| `python generate_schedule.py` | Rebuild the message list and print a preview |
| `python greenapi.py status` | Check WhatsApp is linked (should say `authorized`) |
| `python greenapi.py groups` | List your WhatsApp groups and their IDs |
| `python greenapi.py test "Hi 🌴"` | Send a test message to the group |
| `python greenapi.py today` | Send today's scheduled message now (if there is one) |
| `python greenapi.py shortcut` | Print the URL to paste into the iPhone shortcut |

## iPhone setup (already done)

**Shortcut "Trip Counter"** in the Shortcuts app:

1. **Text**: the contents of `countdown_schedule.json`
2. **Get Dictionary from Input**: from the Text
3. **Get Dictionary Value**: key = **Current Date**, formatted Custom `yyyy-MM-dd`
4. **If** Dictionary Value **has any value**
5. &nbsp;&nbsp;&nbsp;**Get Contents of URL**: URL from `python greenapi.py shortcut`, Method **POST**, Body **JSON**:
   - `chatId` = your group ID (from `python greenapi.py groups`, ends in `@g.us`)
   - `message` = **Dictionary Value**
6. **End If**

**Automation:** Automation tab → Time of Day → **9:00 AM, Daily** → **Run Immediately** → Trip Counter.

Pressing ▶ on a day with no message shows nothing. That's expected.

## Changing messages or dates

1. Edit `config.json` (dates, times) or `messages.py` (wording).
2. Run `python generate_schedule.py` and check the preview.
3. Copy the new `countdown_schedule.json` into the shortcut's **Text** action, replacing the old text.

## Keep it working

- The iPhone needs to be **on with internet** at 9 AM. It can be locked.
- Don't remove Green API from WhatsApp → Settings → **Linked Devices**.
- Green API free Developer plan: up to **3 chats** (currently used: the trip group and your own chat).
- 🔒 The Green API token is in `greenapi_secrets.json` and in the shortcut URL. Don't share either. Reset the token on green-api.com after the trip.

## Full schedule

| Date | Days left | Message |
|---|---|---|
| 26 Oct | 60 | Save those leaves! 🗓️ 60 days left for the trip |
| 5 Nov | 50 | 50 days left for the trip! ✈️ |
| 15 Nov | 40 | 40 days to Sri Lanka 🌴 |
| 25 Nov | 30 | Tick tock ⏰ 30 days until we land in Sri Lanka! |
| 5 Dec | 20 | 🚨 20 days to Sri Lanka! The final countdown begins NOW 🌴 |
| 6 Dec | 19 | Only 19 days left — is everyone's passport ready? 🛂 |
| 7 Dec | 18 | 🔥 Final stretch! Just 18 days to Sri Lanka! |
| 8 Dec | 17 | 17 days! Time to start the packing list 📝 |
| 9 Dec | 16 | 16 days until curry, coconuts & coastline 🥥🍛 |
| 10 Dec | 15 | Countdown mode ON ⚡ 15 days left! |
| 11 Dec | 14 | 14 days — who's making the trip playlist? 🎶 |
| 12 Dec | 13 | Almost there! 13 days to Sri Lanka ✈️ |
| 13 Dec | 12 | 12 days until tea plantations & train rides 🍵🚂 |
| 14 Dec | 11 | 11 days to go! Don't forget the power adapters 🔌 |
| 15 Dec | 10 | 🔟 10 days left — single digits from tomorrow! Sri Lanka, get ready! |
| 16 Dec | 9 | Can you feel it? 9 days to Sri Lanka 🌴🌊 |
| 17 Dec | 8 | Holiday mode loading… 8 days remaining ⏳ |
| 18 Dec | 7 | 📆 ONE WEEK to go! Sri Lanka in 7 days — 7 nights of paradise ahead 🌴 |
| 19 Dec | 6 | 6 days — currency exchanged yet? 💱 |
| 20 Dec | 5 | 5 days left. Check your bookings & tickets 🎫 |
| 21 Dec | 4 | So close! 4 days to Sri Lanka 🌴 |
| 22 Dec | 3 | 3️⃣ days! Start packing for real now 🧳 |
| 23 Dec | 2 | Just 2 days left!! Double-check passports & tickets 🛂🎫 Flight is at 9:50 AM on 25 Dec |
| 24 Dec | 1 | 🛫 TOMORROW we fly to Sri Lanka! Flight at 9:50 AM — don't be late to the airport ⏰🌴🎉 |

"""Message templates. Placeholders: {days}, {destination}, {emoji},
{flight_time}, {trip_date}, {nights}, {return_date}, {return_flight_time}."""

# Used when more than 20 days remain (posted on multiples of 10).
REGULAR = [
    "{days} days to {destination} {emoji}",
    "{days} days left for the trip! ✈️",
    "Only {days} sleeps until {destination}! 😴➡️{emoji}",
    "Countdown check: {days} days to go 🧳",
    "Tick tock ⏰ {days} days until we land in {destination}!",
    "{days} days… start planning those outfits 😎",
    "Mark your calendars 📅 — {days} days to {destination}!",
    "Fun fact: we're just {days} days away from {destination} {emoji}",
    "T-minus {days} days 🚀 {destination}, here we come!",
    "{days} more days of work, then {destination} beaches 🏖️",
    "Save those leaves! 🗓️ {days} days left for the trip",
    "{destination} is calling 📞 and it's only {days} days away!",
]

# Used daily when 20 or fewer days remain.
FINAL = [
    "🔥 Final stretch! Just {days} days to {destination}!",
    "Only {days} days left — is everyone's passport ready? 🛂",
    "{days} days! Time to start the packing list 📝",
    "Can you feel it? {days} days to {destination} {emoji}🌊",
    "{days} days to go — sunscreen bought yet? ☀️🧴",
    "The wait is almost over… {days} days! 🤩",
    "{days} days until curry, coconuts & coastline 🥥🍛",
    "Countdown mode ON ⚡ {days} days left!",
    "{days} days — who's making the trip playlist? 🎶",
    "Almost there! {days} days to {destination} ✈️",
    "{days} days left. Check your bookings & tickets 🎫",
    "Holiday mode loading… {days} days remaining ⏳",
    "{days} days! Dreaming of {destination} sunsets 🌅",
    "Just {days} days — cameras charged? 📸",
    "{days} days to go! Don't forget the power adapters 🔌",
    "So close! {days} days to {destination} {emoji}",
    "{days} days — currency exchanged yet? 💱",
    "Get excited! 🎉 Only {days} days left!",
    "{days} days until tea plantations & train rides 🍵🚂",
    "Bags out of the cupboard yet? {days} days to go 🎒",
]

# Fixed messages for milestone days (override the pools).
SPECIAL = {
    20: "🚨 20 days to {destination}! The final countdown begins NOW {emoji}",
    10: "🔟 10 days left — single digits from tomorrow! {destination}, get ready!",
    7: "📆 ONE WEEK to go! {destination} in 7 days — {nights} nights of paradise ahead {emoji}",
    3: "3️⃣ days! Start packing for real now 🧳",
    2: "Just 2 days left!! Double-check passports & tickets 🛂🎫 Flight is at {flight_time} on {trip_date}",
    1: "🛫 TOMORROW we fly to {destination}! Flight at {flight_time} — don't be late to the airport ⏰{emoji}🎉",
}

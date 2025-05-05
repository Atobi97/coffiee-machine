import streamlit as st

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0


def check_resources(drink):
    for item in drink["ingredients"]:
        if resources.get(item, 0) < drink["ingredients"][item]:
            return False, f"Sorry there's not enough {item}."
    return True, "Resources are sufficient."


def process_coins(quarters, dimes, nickels, pennies):
    return round(quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01, 2)


def check_transaction(user_payment, drink_price):
    global profit
    change = user_payment - drink_price
    if user_payment >= drink_price:
        profit += drink_price
        return True, round(change, 2)
    else:
        return False, 0.0


def make_coffee(drink):
    for item in drink["ingredients"]:
        resources[item] -= drink["ingredients"][item]

# --- Streamlit UI ---


st.title("☕ Coffee Machine App")
drink_choice = st.selectbox("Choose your drink:", list(MENU.keys()))
drink = MENU[drink_choice]
st.write(f"💲 Cost: ${drink['cost']}")

st.subheader("Insert Coins")
col1, col2, col3, col4 = st.columns(4)
with col1:
    quarters = st.number_input("Quarters", 0, 20, 0)
with col2:
    dimes = st.number_input("Dimes", 0, 20, 0)
with col3:
    nickels = st.number_input("Nickels", 0, 20, 0)
with col4:
    pennies = st.number_input("Pennies", 0, 20, 0)

payment = process_coins(quarters, dimes, nickels, pennies)
price = drink["cost"]

st.info(f"💰 Total inserted: ${payment:.2f}")
if payment < price:
    st.warning(f"🚫 You need ${price - payment:.2f} more to buy a {drink_choice}.")
elif payment == price:
    st.success(f"✅ Exact amount! Click 'Make Coffee' to continue.")
else:
    st.success(f"✅ Enough money! You’ll get ${payment - price:.2f} back in change.")

if st.button("Make Coffee"):
    enough, msg = check_resources(drink)
    if not enough:
        st.error(msg)
    else:
        success, change = check_transaction(payment, drink["cost"])
        if success:
            make_coffee(drink)
            st.success(f"Here is your {drink_choice} ☕ Enjoy!")
            if change > 0:
                st.info(f"Your change is ${change}")
        else:
            st.error("Sorry, that's not enough money. Money refunded.")

st.markdown("---")
st.subheader("📊 Machine Report")
st.write(f"Water: {resources['water']}ml")
st.write(f"Milk: {resources.get('milk', 0)}ml")
st.write(f"Coffee: {resources['coffee']}g")
st.write(f"Money: ${profit}")

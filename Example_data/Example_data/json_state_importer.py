from datamodel import Listing, OrderDepth, Trade, TradingState
import json
# Opening JSON file

def import_state(file_name):
	f = open(f"Example_data/{file_name}")
	data = json.load(f)
	f.close()

	listings = {
		product: Listing(
		symbol=product, 
		product=product, 
		denomination=dict(data["listings"])[product]["denomination"]
		) for product in dict(data["listings"])
	}

	order_depths = {
		product: OrderDepth(
			dict(data["order_depths"])[product]["buy_orders"],
			dict(data["order_depths"])[product]["sell_orders"]
		) for product in dict(data["order_depths"])

	}



	market_trades = {
		product: [
			Trade(
				symbol=data["market_trades"][product][trade]["symbol"],
				price=data["market_trades"][product][trade]["price"],
				quantity=data["market_trades"][product][trade]["quantity"],
				buyer=data["market_trades"][product][trade]["buyer"],
				seller=data["market_trades"][product][trade]["seller"],
				timestamp=data["market_trades"][product][trade]["timestamp"]
			) for trade in range(len(data["market_trades"][product]))

		] for product in dict(data["market_trades"])
	}

	own_trades = {
		product: [
			Trade(
				symbol=data["own_trades"][product][trade]["symbol"],
				price=data["own_trades"][product][trade]["price"],
				quantity=data["own_trades"][product][trade]["quantity"],
				buyer=data["own_trades"][product][trade]["buyer"],
				seller=data["own_trades"][product][trade]["seller"],
				timestamp=data["own_trades"][product][trade]["timestamp"]
			) for trade in range(len(data["market_trades"][product]))

		] for product in dict(data["own_trades"])
	}

	state = TradingState(
		timestamp=data["timestamp"],
		listings= listings,
		order_depths=order_depths,
		own_trades=own_trades,
		market_trades=market_trades,
		position=dict(data["position"]),
		observations=dict(data["observations"])
	)

	return state

if __name__ == "__main__":
	a = import_state("example_data.json")
	print(a.toJSON())
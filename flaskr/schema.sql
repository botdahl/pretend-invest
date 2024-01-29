DROP TABLE IF EXISTS tracked_stocks;

CREATE TABLE tracked_stocks (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	stock_name TEXT UNIQUE NOT NULL,
	stock_saved_price DECIMAL NOT NULL
);

INSERT INTO tracked_stocks (stock_name, stock_saved_price) VALUES (%s, %s), ('GME', 14);

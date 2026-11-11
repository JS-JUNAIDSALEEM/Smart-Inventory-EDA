
import unittest
import pandas as pd

from main import validate_data


class TestInventoryData(unittest.TestCase):

    def setUp(self):

        self.df = pd.DataFrame([
            {
                "Transaction_ID": 1,
                "Date": pd.to_datetime("2026-01-01"),
                "Product": "Mouse",
                "Movement_Type": "Stock Out",
                "Quantity": 5
            },
            {
                "Transaction_ID": 2,
                "Date": pd.to_datetime("2026-01-02"),
                "Product": "Keyboard",
                "Movement_Type": "Stock In",
                "Quantity": 10
            }
        ])

        self.opening_stock = {
            "Mouse": 100,
            "Keyboard": 80
        }

        self.reorder_level = {
            "Mouse": 50,
            "Keyboard": 35
        }


# Test 1: Valid transaction data

    def test_valid_data(self):

        results = validate_data(
            self.df,
            self.opening_stock,
            self.reorder_level
        )

        self.assertTrue(all(results.values()))


# Test 2: Duplicate transaction IDs

    def test_duplicate_transaction_ids(self):

        self.df.loc[1, "Transaction_ID"] = 1

        results = validate_data(
            self.df,
            self.opening_stock,
            self.reorder_level
        )

        self.assertFalse(results["Unique Transaction IDs"])


# Test 3: Negative quantities

    def test_negative_quantities(self):

        self.df.loc[0, "Quantity"] = -5

        results = validate_data(
            self.df,
            self.opening_stock,
            self.reorder_level
        )

        self.assertFalse(results["No Negative Quantities"])


# Test 4: Missing values

    def test_missing_values(self):

        self.df.loc[0, "Product"] = None

        results = validate_data(
            self.df,
            self.opening_stock,
            self.reorder_level
        )

        self.assertFalse(results["No Missing Values"])


# Test 5: Invalid movement types

    def test_invalid_movement_types(self):

        self.df.loc[0, "Movement_Type"] = "Transfer"

        results = validate_data(
            self.df,
            self.opening_stock,
            self.reorder_level
        )

        self.assertFalse(results["Valid Movement Types"])


# Test 6: Invalid dates

    def test_invalid_dates(self):

        self.df.loc[0, "Date"] = pd.NaT

        results = validate_data(
            self.df,
            self.opening_stock,
            self.reorder_level
        )

        self.assertFalse(results["Valid Dates"])


# Test 7: Unknown products

    def test_invalid_products(self):

        self.df.loc[0, "Product"] = "Laptop"

        results = validate_data(
            self.df,
            self.opening_stock,
            self.reorder_level
        )

        self.assertFalse(results["Valid Products"])


if __name__ == "__main__":
    unittest.main()

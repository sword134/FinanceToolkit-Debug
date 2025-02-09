"""Toolkit Controller Tests""" ""
import pandas as pd

from financetoolkit import Toolkit

balance_dataset = pd.read_pickle("tests/base/datasets/balance_dataset.pickle")
income_dataset = pd.read_pickle("tests/base/datasets/income_dataset.pickle")
cash_dataset = pd.read_pickle("tests/base/datasets/cash_dataset.pickle")

# pylint: disable=missing-function-docstring


def test_toolkit_balance(recorder):
    toolkit = Toolkit(tickers=["AAPL", "MSFT"], balance=balance_dataset)

    recorder.capture(toolkit.get_balance_sheet_statement())


def test_toolkit_income(recorder):
    toolkit = Toolkit(tickers=["AAPL", "MSFT"], income=income_dataset)

    recorder.capture(toolkit.get_income_statement())


def test_toolkit_cash(recorder):
    toolkit = Toolkit(tickers=["AAPL", "MSFT"], cash=cash_dataset)

    recorder.capture(toolkit.get_cash_flow_statement())


def test_toolkit_ratios(recorder):
    toolkit = Toolkit(
        tickers=["AAPL", "MSFT"],
        balance=balance_dataset,
        income=income_dataset,
        cash=cash_dataset,
    )

    recorder.capture(toolkit.ratios.get_debt_to_assets_ratio())


def test_toolkit_models(recorder):
    toolkit = Toolkit(
        tickers=["AAPL", "MSFT"],
        balance=balance_dataset,
        income=income_dataset,
        cash=cash_dataset,
    )

    recorder.capture(toolkit.models.get_dupont_analysis())

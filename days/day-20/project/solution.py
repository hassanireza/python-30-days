"""
Day 20 Project: Bank Account System
=====================================
OOP bank account with transaction history.
"""
from datetime import datetime


class InsufficientFundsError(Exception):
    """Raised when account has insufficient funds."""


class BankAccount:
    """A simple bank account with transaction history.

    Attributes:
        owner: Full name of the account holder.
        account_number: Unique account identifier.
        balance: Current balance (read-only via property).
    """

    _next_account_number = 1000

    def __init__(self, owner: str, initial_deposit: float = 0.0) -> None:
        self.owner = owner
        self.account_number = BankAccount._next_account_number
        BankAccount._next_account_number += 1
        self._balance = 0.0
        self._transactions: list[dict] = []
        if initial_deposit > 0:
            self.deposit(initial_deposit)

    @property
    def balance(self) -> float:
        """Current account balance (read-only)."""
        return self._balance

    def _record(self, kind: str, amount: float, note: str = "") -> None:
        self._transactions.append({
            "type": kind,
            "amount": amount,
            "balance": self._balance,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "note": note,
        })

    def deposit(self, amount: float) -> None:
        """Deposit a positive amount into the account."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount
        self._record("DEPOSIT", amount)

    def withdraw(self, amount: float) -> None:
        """Withdraw from the account if funds are sufficient."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self._balance:
            raise InsufficientFundsError(
                f"Tried to withdraw ${amount:.2f}, but balance is ${self._balance:.2f}"
            )
        self._balance -= amount
        self._record("WITHDRAW", amount)

    def transfer(self, amount: float, target: "BankAccount") -> None:
        """Transfer funds to another account."""
        self.withdraw(amount)
        target.deposit(amount)
        self._transactions[-1]["note"] = f"to #{target.account_number}"
        target._transactions[-1]["note"] = f"from #{self.account_number}"

    def statement(self) -> str:
        """Return a formatted account statement."""
        lines = [
            f"\n{'=' * 50}",
            f"  Account: #{self.account_number} | Owner: {self.owner}",
            f"  Current Balance: ${self._balance:,.2f}",
            f"{'=' * 50}",
            f"  {'Type':<10} {'Amount':>10} {'Balance':>10}  Time",
            f"  {'-' * 46}",
        ]
        for t in self._transactions:
            sign = "+" if t["type"] == "DEPOSIT" else "-"
            note = f" ({t['note']})" if t["note"] else ""
            lines.append(
                f"  {t['type']:<10} {sign}${t['amount']:>8.2f} ${t['balance']:>9.2f}  {t['time']}{note}"
            )
        lines.append("=" * 50)
        return "\n".join(lines)

    def __repr__(self) -> str:
        return f"BankAccount(owner={self.owner!r}, balance=${self._balance:.2f})"


def main() -> None:
    alice = BankAccount("Alice Johnson", initial_deposit=1000.0)
    bob = BankAccount("Bob Smith", initial_deposit=500.0)

    alice.deposit(250.0)
    alice.withdraw(100.0)
    alice.transfer(200.0, bob)

    print(alice.statement())
    print(bob.statement())


if __name__ == "__main__":
    main()

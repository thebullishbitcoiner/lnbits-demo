#
#   Written by Pavel Kononov from LightningBounties.com
#   For MIT Bitcoin Hackathon 2025
#
#   Happy hacking!
#

from dataclasses import dataclass
from datetime import datetime
from typing import Any


@dataclass
class Account:
    id: str
    user: str
    name: str
    adminkey: str
    inkey: str
    deleted: bool
    currency: str
    balance_msat: int
    created_at: datetime | None = None
    updated_at: datetime | None = None
    extra: dict | None = None


@dataclass
class Wallet:
    id: str
    user: str
    name: str
    adminkey: str
    inkey: str
    deleted: bool
    currency: str
    balance_msat: int
    created_at: datetime | None = None
    updated_at: datetime | None = None
    extra: dict | None = None


@dataclass
class WalletInfo:
    name: str
    balance: int


@dataclass
class Invoice:
    payment_hash: str
    payment_request: str
    checking_id: str
    lnurl_response: Any | None = None
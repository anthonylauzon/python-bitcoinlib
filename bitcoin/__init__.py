# Copyright (C) 2012-2017 The python-bitcoinlib developers
#
# This file is part of python-bitcoinlib.
#
# It is subject to the license terms in the LICENSE file found in the top-level
# directory of this distribution.
#
# No part of python-bitcoinlib, including this file, may be copied, modified,
# propagated, or distributed except according to the terms contained in the
# LICENSE file.

from __future__ import absolute_import, division, print_function, unicode_literals

import bitcoin.core

# Note that setup.py can break if __init__.py imports any external
# dependencies, as these might not be installed when setup.py runs. In this
# case __version__ could be moved to a separate version.py and imported here.
__version__ = '0.9.1dev'

class MainParams(bitcoin.core.CoreMainParams):
    MESSAGE_START = b'\xf9\xbe\xb4\xd9'
    DEFAULT_PORT = 8333
    RPC_PORT = 8332
    DNS_SEEDS = (('bitcoin.sipa.be', 'seed.bitcoin.sipa.be'),
                 ('bluematt.me', 'dnsseed.bluematt.me'),
                 ('dashjr.org', 'dnsseed.bitcoin.dashjr.org'),
                 ('bitcoinstats.com', 'seed.bitcoinstats.com'),
                 ('xf2.org', 'bitseed.xf2.org'),
                 ('bitcoin.jonasschnelli.ch', 'seed.bitcoin.jonasschnelli.ch'),
                 ('btc.petertodd.org', "seed.btc.petertodd.org"))
    BASE58_PREFIXES = {'PUBKEY_ADDR':0,
                       'SCRIPT_ADDR':5,
                       'SECRET_KEY' :128}

class TestNetParams(bitcoin.core.CoreTestNetParams):
    MESSAGE_START = b'\x0b\x11\x09\x07'
    DEFAULT_PORT = 18333
    RPC_PORT = 18332
    DNS_SEEDS = (('testnetbitcoin.jonasschnelli.ch', 'testnet-seed.bitcoin.jonasschnelli.ch'),
                 ('petertodd.org', 'seed.tbtc.petertodd.org'),
                 ('bluematt.me', 'testnet-seed.bluematt.me'),
                 ('bitcoin.schildbach.de', 'testnet-seed.bitcoin.schildbach.de'))
    BASE58_PREFIXES = {'PUBKEY_ADDR':111,
                       'SCRIPT_ADDR':196,
                       'SECRET_KEY' :239}

class RegTestParams(bitcoin.core.CoreRegTestParams):
    MESSAGE_START = b'\xfa\xbf\xb5\xda'
    DEFAULT_PORT = 18444
    RPC_PORT = 18332
    DNS_SEEDS = ()
    BASE58_PREFIXES = {'PUBKEY_ADDR':111,
                       'SCRIPT_ADDR':196,
                       'SECRET_KEY' :239}

class LitecoinMainParams(bitcoin.core.CoreMainParams):
    NAME = 'ltc_mainnet'
    MESSAGE_START = b'\xfb\xc0\xb6\xdb'
    DEFAULT_PORT = 9333
    RPC_PORT = 9332
    DNS_SEEDS = (('litecoin.loshan.co.uk', 'seed-a.litecoin.loshan.co.uk'),
                 ('thrasher.io', 'dnsseed.thrasher.io'),
                 ('litecointools.com', 'dnsseed.litecointools.com'),
                 ('litecoinpool.org', 'dnsseed.litecoinpool.org'),
                 ('koin-project.com', 'dnsseed.koin-project.com'))
    BASE58_PREFIXES = {'PUBKEY_ADDR':48,
                       'SCRIPT_ADDR':5,
                       'SECRET_KEY' :176}

class LitecoinTestNetParams(bitcoin.core.CoreTestNetParams):
    NAME = 'ltc_testnet'
    MESSAGE_START = b'\xfd\xd2\xc8\xf1'
    DEFAULT_PORT = 19335
    RPC_PORT = 19332
    DNS_SEEDS = (('litecointools.com', 'testnet-seed.litecointools.com'),
                 ('litecoin.loshan.co.uk', 'seed-b.litecoin.loshan.co.uk'),
                 ('thrasher.io', 'dnsseed-testnet.thrasher.io'))
    BASE58_PREFIXES = {'PUBKEY_ADDR':111,
                       'SCRIPT_ADDR':196,
                       'SECRET_KEY' :239}



"""Master global setting for what chain params we're using.

However, don't set this directly, use SelectParams() instead so as to set the
bitcoin.core.params correctly too.
"""
#params = bitcoin.core.coreparams = MainParams()
params = MainParams()

def SelectParams(name):
    """Select the chain parameters to use

    name is one of 'mainnet', 'testnet', or 'regtest'

    Default chain is 'mainnet'
    """
    global params
    bitcoin.core._SelectCoreParams(name)
    if name == 'mainnet':
        params = bitcoin.core.coreparams = MainParams()
    elif name == 'testnet':
        params = bitcoin.core.coreparams = TestNetParams()
    elif name == 'regtest':
        params = bitcoin.core.coreparams = RegTestParams()
    elif name == 'ltc_mainnet':
        params = bitcoin.core.coreparams = LitecoinMainParams()
    elif name == 'ltc_testnet':
        params = bitcoin.core.coreparams = LitecoinTestNetParams()
    else:
        raise ValueError('Unknown chain %r' % name)

def get_params():
    global params
    return params

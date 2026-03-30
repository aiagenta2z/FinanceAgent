import asyncio
import json
import types
from starlette.applications import Starlette
from starlette.exceptions import HTTPException
from starlette.responses import JSONResponse, StreamingResponse
from starlette.responses import JSONResponse
from starlette.routing import Mount, Route
from starlette.staticfiles import StaticFiles
from starlette.requests import Request
from mcp.server.fastmcp import FastMCP
import contextlib
import os

### --------- chat endpoint to use in Agent Router ------
from pydantic import BaseModel, Field
from typing import Any, Dict, List, Optional, Tuple, Union

from FinanceAgent import KEY_SYMBOL_LIST

AGENT_NAME="FinanceAgent"

### api function list
import FinanceAgent as fa

KEY_SYMBOL_LIST = "symbol_list"

async def get_hk_stock_market_hkex(request):
    """
        Get HongKong Stock Market, HKEX
        Args:
            symbol_list (List[Str]): list of stock symbols

        Return:
            [{'symbol': 'SH600036',
              'current': 39.48,
              'percent': 0.1,
              'chg': 0.04,
              'high': '39.55 CNY',
              'low': '39.13 CNY',
              'avg_price': '39.3356485359752 CNY',
              'timestamp': 1774841399710,
              'open': 39.24,
              'last_close': 39.44,
              'market_capital': 995679504327.0,
              'change': '0.04(0.1%)',
              'previous_close': '39.44 CNY',
              'market_capitalization': '9956.80 亿 CNY',
              'pe_ratio': '',
              'update_time': '2026-03-30 11:29:59',
              'source': 'XUEQIU.COM, https://xueqiu.com/S/SH600036',
              'data_source': 'xueqiu.com',
              'source_url': 'https://xueqiu.com/S/SH600036'},
             {'symbol': 'SH600519',
              'current': 1425.15,
              'percent': 0.64,
              'chg': 9.13,
              'high': '1431.0 CNY',
              'low': '1402.52 CNY',
              'avg_price': '1413.4029095763897 CNY',
              'timestamp': 1774841395430,
              'open': 1407.0,
              'last_close': 1416.02,
              'market_capital': 1784672896907.0,
              'change': '9.13(0.64%)',
              'previous_close': '1416.02 CNY',
              'market_capitalization': '17846.73 亿 CNY',
              'pe_ratio': '',
              'update_time': '2026-03-30 11:29:55',
              'source': 'XUEQIU.COM, https://xueqiu.com/S/SH600519',
              'data_source': 'xueqiu.com',
              'source_url': 'https://xueqiu.com/S/SH600519'}]
    """
    result = {}
    try:
        body = {}
        try:
            body = await request.json()
        except json.JSONDecodeError:
            raise HTTPException(status_code=400, detail="Invalid JSON body")
        symbol_list = body.get(KEY_SYMBOL_LIST, [])
        ## list
        print (f"INFO: API Calling get_hk_stock_market_hkex input symbol_list {symbol_list}")
        stock_info = fa.api(symbol_list=symbol_list, market="HK")
        result["success"] = True
        result["data"] = stock_info
    except Exception as e:
        result["success"] = False
        result["data"] = []
        result["message"] = "Calling Internal API Failed..."
    return JSONResponse(result)

async def get_cn_stock_market_shanghai_shenzhen(request):
    """
        cn_stock_info_json = fa.api(symbol_list=['SH600519', 'SH600036'], market="CN_MAINLAND")

        Args:
            request (Request): starlette request

        Return:
            JSONResponse
    """
    result = {}
    try:
        body = {}
        try:
            body = await request.json()
        except json.JSONDecodeError:
            raise HTTPException(status_code=400, detail="Invalid JSON body")
        symbol_list = body.get(KEY_SYMBOL_LIST, [])
        print (f"INFO: API Calling get_cn_stock_market_shanghai_shenzhen input symbol_list {symbol_list}")
        stock_info = fa.api(symbol_list=symbol_list, market="CN_MAINLAND")
        result["success"] = True
        result["data"] = stock_info
    except Exception as e:
        result["success"] = False
        result["data"] = []
        result["message"] = "Calling Internal API Failed..."
    return JSONResponse(result)

async def get_us_stock_market_nyse_nasdaq_dow(request):
    """
        Get US Stock Marketplace: NYSE, NASDAQ, DOW
        us_stock_info_json = fa.api(symbol_list=['TSLA', 'MSFT', 'GOOG'], market="US")

        Args:
            request (Request): starlette request
        Return:
            JSONResponse
    """
    result = {}
    try:
        body = {}
        try:
            body = await request.json()
        except json.JSONDecodeError:
            raise HTTPException(status_code=400, detail="Invalid JSON body")
        symbol_list = body.get(KEY_SYMBOL_LIST, [])
        print (f"INFO: API Calling get_us_stock_market_nyse_nasdaq_dow input symbol_list {symbol_list}")
        stock_info = fa.api(symbol_list=symbol_list, market="US")
        result["success"] = True
        result["data"] = stock_info
    except Exception as e:
        result["success"] = False
        result["data"] = []
        result["message"] = "Calling Internal API Failed..."
    return JSONResponse(result)

async def get_uk_stock_market_lse(request):
    """
        Get US Stock Marketplace: NYSE, NASDAQ, DOW
        lse_stock_info_json = fa.api(symbol_list=['SHEL', 'ULVR'], market="LSE")

        Args:
            request (Request): starlette request
        Return:
            JSONResponse
    """
    result = {}
    try:
        body = {}
        try:
            body = await request.json()
        except json.JSONDecodeError:
            raise HTTPException(status_code=400, detail="Invalid JSON body")
        symbol_list = body.get(KEY_SYMBOL_LIST, [])
        print (f"INFO: API Calling get_uk_stock_market_lse input symbol_list {symbol_list}")
        stock_info = fa.api(symbol_list=symbol_list, market="LSE")
        result["success"] = True
        result["data"] = stock_info
    except Exception as e:
        result["success"] = False
        result["data"] = []
        result["message"] = "Calling Internal API Failed..."
    return JSONResponse(result)

async def get_india_stock_market_nse_india(request):
    """
        Get US Stock Marketplace: NYSE, NASDAQ, DOW
        india_stock_info_json = fa.api(symbol_list=['TM03', 'IT'], market="NSE_INDIA")

        Args:
            request (Request): starlette request
        Return:
            JSONResponse
    """
    result = {}
    try:
        body = {}
        try:
            body = await request.json()
        except json.JSONDecodeError:
            raise HTTPException(status_code=400, detail="Invalid JSON body")
        symbol_list = body.get(KEY_SYMBOL_LIST, [])
        print (f"INFO: API Calling get_india_stock_market_nse_india input symbol_list {symbol_list}")
        stock_info = fa.api(symbol_list=symbol_list, market="NSE_INDIA")
        result["success"] = True
        result["data"] = stock_info
    except Exception as e:
        result["success"] = False
        result["data"] = []
        result["message"] = "Calling Internal API Failed..."
    return JSONResponse(result)

### --------- mcp endpoint to use in clients ------
mcp = FastMCP(AGENT_NAME, json_response=True)

@mcp.tool()
def get_hk_stock_market_hkex_mcp(
    symbol_list: List[str]
) -> Dict:
    """
    Args:
        symbol_list=['700', '1024']
    Returns:
    """
    return fa.api(symbol_list=symbol_list, market="HK")

@mcp.tool()
def get_cn_stock_market_shanghai_shenzhen_mcp(
    symbol_list: List[str]
) -> Dict:
    """
    Args:
        symbol_list=['700', '1024']
    Returns:

    """
    return fa.api(symbol_list=symbol_list, market="CN_MAINLAND")

@mcp.tool()
def get_us_stock_market_nyse_nasdaq_dow_mcp(
    symbol_list: List[str]
) -> Dict:
    """
    Args:
        symbol_list=['700', '1024']
    Returns:

    """
    return fa.api(symbol_list=symbol_list, market="US")

@mcp.tool()
def get_uk_stock_market_lse_mcp(
    symbol_list: List[str]
) -> Dict:
    """
    Args:
        symbol_list=['700', '1024']
    Returns:

    """
    return fa.api(symbol_list=symbol_list, market="LSE")

@mcp.tool()
def get_india_stock_market_nse_india_mcp(
    symbol_list: List[str]
) -> Dict:
    """
    Args:
        symbol_list=['700', '1024']
    Returns:
    """
    return fa.api(symbol_list=symbol_list, market="NSE_INDIA")

mcp_app = mcp.streamable_http_app()

@contextlib.asynccontextmanager
async def lifespan(app: Starlette):
    # STARTUP: Initialize Perplexity Agent
    print("--- APPLICATION STARTUP ---")
    # Agent is already initialized at module level
    # If needed, we can add async initialization here

    async with mcp.session_manager.run():
        yield

    # SHUTDOWN: Cleanup
    print("--- APPLICATION SHUTDOWN ---")
    # PerplexityAgent doesn't require explicit cleanup


app = Starlette(
    routes=[
        Route("/api/v1/get_hk_stock_market_hkex", get_hk_stock_market_hkex, methods=["GET", "POST"]),
        Route("/api/v1/get_cn_stock_market_shanghai_shenzhen", get_cn_stock_market_shanghai_shenzhen, methods=["GET", "POST"]),
        Route("/api/v1/get_us_stock_market_nyse_nasdaq_dow", get_us_stock_market_nyse_nasdaq_dow, methods=["GET", "POST"]),
        Route("/api/v1/get_uk_stock_market_lse", get_uk_stock_market_lse, methods=["GET", "POST"]),
        Route("/api/v1/get_india_stock_market_nse_india", get_india_stock_market_nse_india, methods=["GET", "POST"]),
        Mount("/", app=mcp_app),  ## MCP Endpoint Always mounts /mcp
    ],
    lifespan=lifespan,
)


def main():
    """

    :return:
    """

if __name__ == '__main__':
    main()
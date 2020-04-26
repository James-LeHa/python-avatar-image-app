import unittest
from codeApp import format_query, run_query
import pytest

def test_userQuery():
    userName = "izzyco" 
    query = format_query(userName)
    result = run_query(query)
    avatarUrlReturned = result["data"]["user"]["avatarUrl"] 
    print('Avatar URL Returned: ' + avatarUrlReturned)
    assert avatarUrlReturned
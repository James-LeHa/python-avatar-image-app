import unittest
from codeApp import format_queryUser, run_query
import pytest

def test_userQuery():
    userName = "izzyco" 
    query = format_queryUser(userName)
    result = run_query(query)
    avatarUrlReturned = result["data"]["user"]["avatarUrl"] 
    print('Avatar URL Returned: ' + avatarUrlReturned)
    assert avatarUrlReturned
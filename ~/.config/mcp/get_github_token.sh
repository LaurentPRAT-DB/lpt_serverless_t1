#!/bin/bash
# Script to securely retrieve GitHub token from macOS keychain
security find-generic-password -a $USER -s github-mcp-token -w

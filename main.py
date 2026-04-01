import os
from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="LinkedIn Proxy")


class InvitationRequest(BaseModel):
    profile_url: str
    full_name: Optional[str] = None


class MessageRequest(BaseModel):
    profile_url: str
    message: str


@app.get("/")
async def root():
    return {
        "message": "LinkedIn proxy is running",
        "docs": "/docs",
    }


@app.get("/linkedin/callback")
async def linkedin_callback(code: Optional[str] = None, state: Optional[str] = None):
    if not code:
        raise HTTPException(status_code=400, detail="Missing authorization code")

    return {
        "success": True,
        "message": "LinkedIn callback received",
        "code": code,
        "state": state,
        "next_step": "Exchange this code for an access token in production",
    }


@app.post("/invitations")
async def send_invitation(payload: InvitationRequest):
    # TODO:
    # Replace this mock response with the real LinkedIn API call
    # after your app gets approved for the needed permissions.
    return {
        "success": True,
        "action": "invitation_created",
        "profile_url": payload.profile_url,
        "full_name": payload.full_name,
        "note": "Mock response for now. Wire official LinkedIn API here later.",
    }


@app.post("/messages")
async def send_message(payload: MessageRequest):
    # TODO:
    # Replace this mock response with the real LinkedIn API call
    # after your app gets approved for the needed permissions.
    return {
        "success": True,
        "action": "message_sent",
        "profile_url": payload.profile_url,
        "message": payload.message,
        "note": "Mock response for now. Wire official LinkedIn API here later.",
    }


@app.get("/acceptance-status")
async def acceptance_status(profileUrl: str):
    # TODO:
    # Replace with a real LinkedIn lookup when your API access is approved.
    return {
        "profile_url": profileUrl,
        "status": "accepted",
        "note": "Mock response for now.",
    }

from fastapi import APIRouter
from services.worldbank_service import get_worldbank_metrics
from services.imf_service import get_imf_metrics
from services.sipri_service import get_sipri_metrics

router = APIRouter()

@router.get("/metrics")
def get_metrics(actor: str):
    return {
        "actor": actor,
        "worldbank": get_worldbank_metrics(actor),
        "imf": get_imf_metrics(actor),
        "sipri": get_sipri_metrics(actor)
    }

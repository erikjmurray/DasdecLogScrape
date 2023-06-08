""" Class dfn for EAS Tests """
# --- BUILT-IN IMPORTS ---
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class EasTest:
    id: str
    test_type: str
    full_test_type: str
    ipaws: str
    organization: str
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    decoded_timestamp: Optional[str] = None
    originated_timestamp: Optional[str] = None
    locations: Optional[List[str]] = None


@dataclass
class AllTests:
    originated_tests: List[EasTest] = field(default_factory=list)
    forwarded_tests: List[EasTest] = field(default_factory=list)
    decoded_tests: List[EasTest] = field(default_factory=list)
    eas_net_decoded_tests: List[EasTest] = field(default_factory=list)
    cap_eas_decoded_tests: List[EasTest] = field(default_factory=list)

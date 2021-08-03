# import argparse
from internal_consistency_engine.internal_consistency_engine import CoherencyEngine

# STEP 1
#   Parse command line arguments
#   Load Flat-file configs using command line arguments
#   Load Keystore configs using flat-file information
#       Record call-backs for each config component
#       Establish each configured service and connection
#           Load configuration environment if configuration is invalid
#           Disable all non-configuration environment services and connections if configuration is invalid
#       If configurations are valid, start up operation environment
#       Pass control to operation environment

if __name__ == "__main__":
    engine = CoherencyEngine()
    if engine.validate():
        engine.start()
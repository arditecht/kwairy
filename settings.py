### ---------------------------------------------- ############################
# | SETTINGS TO DETERMINE GLOBAL RUNTIME BEHAVIOUR |			      		  #
###############################################################################


# | NOTE: Precision mode is by-default TRUE while development phase	          #

runtime = {
    "precision_mode" : True, # uses open ai model for inference, use false for cost savings mode
    "local_embed" : True, # Local embeddings are good enough and free to use, or if False, use open ai embeddings
}
             
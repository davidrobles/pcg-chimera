def validate_probs(probs):
    for block_type, d in probs.items():
        if sum(d.values()) != 1.0:
            raise ValueError("{} probs should sum to 1.0: {}".format(block_type, d))
import os


def do_setup():
    os.system("export LANGCHAIN_API_KEY=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")
    os.environ["LANGCHAIN_API_KEY"] = "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"
    os.environ["GROQQ_API_KEY"] = "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"

    return "setup done"
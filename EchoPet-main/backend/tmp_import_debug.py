import importlib, traceback

importlib.invalidate_caches()
try:
    m = importlib.import_module('routes.quiz')
    print('Imported routes.quiz, has quiz_bp =', hasattr(m, 'quiz_bp'))
    print('module dict keys:', list(m.__dict__.keys()))
except Exception:
    traceback.print_exc()
    raise

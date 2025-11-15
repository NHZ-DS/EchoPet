import runpy, pprint

g = runpy.run_path('routes/quiz.py')
print('keys from run_path:', sorted(g.keys()))
print('has quiz_bp?', 'quiz_bp' in g)
if 'quiz_bp' in g:
    print('quiz_bp repr:', repr(g['quiz_bp']))

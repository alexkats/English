# fa_min.py
# Демонстрация работы алгоритма Бржозовского

Q = 0
A = 1
T = 2
S = 3
F = 4

# Вывод КА в формате свободно распространяемой утилиты graphviz

def fa_gv(fa, filename):
    f = open(filename, 'w')
    for i in fa[F]:
        f.write('"' + str(fa[Q][i]) + '";')
    f.write('\nnode[shape=circle];\n');
    for t1 in range(0, len(fa[Q])):
        for a in range(0, len(fa[A])):
            for t2 in fa[T][t1][a]:
                f.write('"' + str(fa[Q][t1]) +'"' + '->' + '"' + \
                        str(fa[Q][t2]) + '"')
                f.write('[label="' + str(fa[A][a]) + '"];\n')
    f.write('}\n')
    f.close()

# Обращение КА

def fa_rev(fa):
    rfa = [list(fa[Q]), list(fa[A]), [], list(fa[F]), list(fa[S])]
    rfa[T] = [[[] for i in range(0, len(fa[A]))] for j in range(0, len(fa[Q]))]
    for t1 in range(0, len(fa[Q])):
        for a in range(0, len(fa[A])):
            for t2 in fa[T][t1][a]:
                rfa[T][t2][a].append(t1)
    return rfa

# Детерминизация КА

def fa_det(fa):
    def reachable(q, l):
        t = []
        for a in range(0, len(fa[A])):
            ts = set()
            for i in q[l]:
                # объединение множеств (достижимых из l) состояний для символа a
                ts |= set(fa[T][i][a])
            if not ts:
                t.append([])
                continue
            try:
                i = q.index(ts)
            except ValueError:
                i = len(q)
                q.append(ts)
            t.append([i])
        return t
    dfa = [[], list(fa[A]), [], [0], []]
    q = [set(fa[S])]
    while len(dfa[T]) < len(q):
        dfa[T].append(reachable(q, len(dfa[T])))
    dfa[Q] = range(0, len(q))
    dfa[F] = [q.index(i) for i in q if set(fa[F]) & i]
    return dfa

# Алгоритм Бржозовского

def fa_min(fa):
    return fa_det(fa_rev(fa_det(fa_rev(fa))))

# Пример работы

fa = [None]*5

fa[Q] = [0, 1]
fa[A] = ['a']
fa[T] = [[[1]], [[1]]]
fa[S] = [0]
fa[F] = [0, 1]

fa_gv(fa_min(fa), 'my.out')

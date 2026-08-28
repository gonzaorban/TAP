# Este hizo Claude, estaba muy duro

import sys
from bisect import bisect_right


def main():
    data = sys.stdin.buffer.read().split()

    n = int(data[0])
    k = int(data[1])

    # un rey solo ocupa una celda: el rectangulo nunca crece
    if n == 1:
        print(1)
        return

    nums = list(map(int, data[2:2 + 2 * n]))
    filas = nums[0::2]
    cols = nums[1::2]

    minR = min(filas)
    maxR = max(filas)
    minC = min(cols)
    maxC = max(cols)

    alto = maxR - minR + 1
    ancho = maxC - minC + 1

    # Un rey que empuja un lado vertical en 'a' y uno horizontal en 'b'
    # gasta max(a + distVert, b + distHoriz): las diagonales avanzan en
    # los dos ejes al mismo tiempo.
    #
    # Para cada esquina guardo, por cada distancia vertical, la menor
    # distancia horizontal. Los reyes a mas de k de un borde no sirven,
    # asi que los descarto en la misma pasada.
    INF = 1 << 62
    sup_izq = {}
    sup_der = {}
    inf_izq = {}
    inf_der = {}
    g_si = sup_izq.get
    g_sd = sup_der.get
    g_ii = inf_izq.get
    g_id = inf_der.get

    for r, c in zip(filas, cols):
        du = r - minR
        dd = maxR - r
        dl = c - minC
        dr = maxC - c
        if du <= k:
            if dl < g_si(du, INF):
                sup_izq[du] = dl
            if dr < g_sd(du, INF):
                sup_der[du] = dr
        if dd <= k:
            if dl < g_ii(dd, INF):
                inf_izq[dd] = dl
            if dr < g_id(dd, INF):
                inf_der[dd] = dr

    # me quedo con los reyes no dominados de cada esquina
    pares = []
    for d in (sup_izq, sup_der, inf_izq, inf_der):
        mejor_dh = None
        for x in sorted(d):
            y = d[x]
            if mejor_dh is None or y < mejor_dh:
                pares.append((x, y))
                mejor_dh = y

    min_dh = min(dh for _, dh in pares)

    # pares ordenados por dv, con el minimo dh acumulado
    pares.sort()
    dvs = [p[0] for p in pares]
    pref_dh = []
    acum = None
    for dv, dh in pares:
        if acum is None or dh < acum:
            acum = dh
        pref_dh.append(acum)

    # base(e) = min sobre pares de max(e + dv, dh).
    # Para un par ese max vale e+dv cuando e >= dh-dv, y dh si no,
    # asi que ordeno por ese umbral y consulto con busqueda binaria.
    umbrales = sorted((dh - dv, dv, dh) for dv, dh in pares)
    thr = [t for t, _, _ in umbrales]
    cant = len(umbrales)

    pref_dv = []
    acum = None
    for _, dv, _ in umbrales:
        if acum is None or dv < acum:
            acum = dv
        pref_dv.append(acum)

    suf_dh = [0] * (cant + 1)
    acum = INF
    for i in range(cant - 1, -1, -1):
        dh = umbrales[i][2]
        if dh < acum:
            acum = dh
        suf_dh[i] = acum
    suf_dh[cant] = INF

    mejor = alto * ancho

    # para cada crecimiento vertical e busco el maximo horizontal f
    for e in range(k + 1):
        fmax = k - e  # sin diagonales: 1 celda por movimiento

        # el mismo rey empuja los dos ejes en diagonal
        j = bisect_right(dvs, k - e) - 1
        if j >= 0:
            v = k - pref_dh[j]
            if v > fmax:
                fmax = v

        # un rey cubre el horizontal y otro el vertical
        v = k - e - min_dh
        if v > fmax:
            fmax = v

        # un rey cubre el vertical y otro el horizontal
        i = bisect_right(thr, e)
        base = suf_dh[i]
        if i > 0:
            otro = e + pref_dv[i - 1]
            if otro < base:
                base = otro
        v = k - base
        if v > fmax:
            fmax = v

        if fmax > k:
            fmax = k
        if fmax >= 0:
            area = (alto + e) * (ancho + fmax)
            if area > mejor:
                mejor = area

    print(mejor)


main()

import math

def modular_sqrt(a, p):
    """ Find a quadratic residue (mod p) of 'a'. p
        must be an odd prime.

        Solve the congruence of the form:
            x^2 = a (mod p)
        And returns x. Note that p - x is also a root.

        0 is returned is no square root exists for
        these a and p.

        The Tonelli-Shanks algorithm is used (except
        for some simple cases in which the solution
        is known from an identity). This algorithm
        runs in polynomial time (unless the
        generalized Riemann hypothesis is false).
    """
    # Simple cases
    #
    if legendre_symbol(a, p) != 1:
        return 0
    elif a == 0:
        return 0
    elif p == 2:
        return p
    elif p % 4 == 3:
        return pow(a, (p + 1) / 4, p)

    # Partition p-1 to s * 2^e for an odd s (i.e.
    # reduce all the powers of 2 from p-1)
    #
    s = p - 1
    e = 0
    while s % 2 == 0:
        s /= 2
        e += 1

    # Find some 'n' with a legendre symbol n|p = -1.
    # Shouldn't take long.
    #
    n = 2
    while legendre_symbol(n, p) != -1:
        n += 1

    # Here be dragons!
    # Read the paper "Square roots from 1; 24, 51,
    # 10 to Dan Shanks" by Ezra Brown for more
    # information
    #

    # x is a guess of the square root that gets better
    # with each iteration.
    # b is the "fudge factor" - by how much we're off
    # with the guess. The invariant x^2 = ab (mod p)
    # is maintained throughout the loop.
    # g is used for successive powers of n to update
    # both a and b
    # r is the exponent - decreases with each update
    #
    x = pow(a, (s + 1) / 2, p)
    b = pow(a, s, p)
    g = pow(n, s, p)
    r = e

    while True:
        t = b
        m = 0
        for m in xrange(r):
            if t == 1:
                break
            t = pow(t, 2, p)

        if m == 0:
            return x

        gs = pow(g, 2 ** (r - m - 1), p)
        g = (gs * gs) % p
        x = (x * gs) % p
        b = (b * g) % p
        r = m


def legendre_symbol(a, p):
    """ Compute the Legendre symbol a|p using
        Euler's criterion. p is a prime, a is
        relatively prime to p (if p divides
        a, then a|p = 0)

        Returns 1 if a has a square root modulo
        p, -1 otherwise.
    """
    ls = pow(a, (p - 1) / 2, p)
    return -1 if ls == p - 1 else ls

def print_table(p, m_range, data):
    l = data[0]
    lines = data[1]
    print "    |       p      |    |      %-8s|\nl = |  ----------  | =  |  ----------  | = %s\n    |_  mmax + 1  _|    |_  %-4s + 1  _|" % (p, l, m_range[1])
    template = "%-10s%-10s%-10s%-10s%-10s%-10s%-10s"
    print template % ("m", "lm", "lm+l-1", "m'", "f(m')", "V(f(m'))", "(x, y)")
    print "-" * 10 * 7
    for line in lines:
        print template % tuple(line)

def elliptic(p, A, B, m_range):
    l = int(math.floor(p / (m_range[1] + 1)))
    data = []
    for m in range(m_range[0], m_range[1] + 1):
        lm = m * l
        lml1 = lm + l - 1
        m2 = "Nothing"
        fm2 = "Nothing"
        Vfm2 = "Nothing"
        for i in range(lm, lml1 + 1):
            fm2 = (i*i*i + A*i + B) % p
            Vfm2 = modular_sqrt(fm2, p)
            if Vfm2:
                m2 = i
                break
        data.append([m, lm, lml1, m2, fm2, Vfm2, (m2, Vfm2)])
    return l, data

if __name__ == "__main__":
    p = 79
    A = 5
    B = 13
    m_range = [0, 4]
    print_table(p, m_range, elliptic(p, A, B, m_range))

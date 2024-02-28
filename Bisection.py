"""
İkiye bölme metodu, tam olarak adının da anlattığı işlemi uygular. Bir f(x) fonksiyonu alınsın. Bu fonksiyon [a,b] kapalı aralığında
sürekli ve a ile b sayıları reel sayılar kümesinin birer elemanı olsun. Eğer bu aralıkta f(a).f(b)<0 oluyorsa, Bolzano teoreminin
bize söylediği üzere bu aralıkta bu fonksiyonun en az bir kökü bulunur.
Kökün bulunduğunu garantiledikten sonra tek yapılması gereken, f(a).f(b)<0 koşulunu, aralığı ikiye bölmeye devam ederek sağlamaktır.
"""
#f = (x-1)**2*(x-2)*(x-3)
#f2 = 2**(x-2)*(x-3) + 4*(x-1)*(2*x-5) + 2*(x-1)**2


def f_prime(x):
    return 2*(x-1)*(x-2)*(x-3) + (x-1)**2*(2*x-5)

def ikiye_bolme(xa, xb, tol):
    if f_prime(xa) * f_prime(xb) > 0:
        raise ValueError("Başlangıç noktaları uygun değil.")

    elif f_prime(xa) == 0:
            return xa

    else:
        while abs(xb - xa) > tol:
            xk = xa + (xb - xa) / 2
            if f_prime(xk) == 0 or abs(xb - xa) < tol:
                return xk
            elif f_prime(xk) * f_prime(xa) > 0:
                xa = xk
            else:
                xb = xk

        return (xa + xb) / 2

# Başlangıç noktalarını belirle
xa = 0
xb = 1
tol=1e-4
# Kökü hesapla
root = ikiye_bolme(xa, xb,tol)

print("Kök:", root)












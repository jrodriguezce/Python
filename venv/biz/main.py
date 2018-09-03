from inheritance.Contact import Contact
from inheritance.Friend import Friend


# ============= EJEMPLO DE HERENCIA ==============
f1 = Friend("Anderson", "Anderson@mail.com", "3118030925")
c2 = Contact("Carlos", "Carlos@mail.com")

print( "Contacto: " + c2.name )
print( "Amigo: " + f1.name )
# ================================================

# ========== EJEMPLO DE ENCAPSULAMIENTO ==========
c2.name = "Julian"
f1.phone = "3119338844"
# ================================================
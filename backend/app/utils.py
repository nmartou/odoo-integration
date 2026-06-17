from models.property import Property

class Print:
    @staticmethod
    def values(objs: list[Property]):
        header = f"id_property      price       property_type       address_id"
        print(header)
        for i in objs:
            val = f"{i.id_property}    {i.price}     {i.property_type}     {i.address_id}"
            print(val)
        
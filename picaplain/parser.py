import datetime
from . import utils


class PicaPlain:

    def __init__(self, plain: str):
        self.plain = plain
        self.rows = self.plain.split("\n")

    def __str__(self):
        return self.plain

    def get_field(self, key, repeat=True):
        return utils.get_field(key, self.rows, repeat=repeat)

    def get_subfield(self, key, subkey, repeat=True, subrepeat=True):
        field = self.get_field(key, repeat=repeat)
        if field:
            if isinstance(field, str):
                return utils.get_subfield(subkey, field, repeat=subrepeat)
            elif isinstance(field, list):
                found = [utils.get_subfield(subkey, f, repeat=subrepeat) for f in field]
                if len(found) > 0 and not all([f is None for f in found]):
                    return found

    def get_subfield_unique(self, key, subkey, repeat=False):
        return self.get_subfield(key, subkey, repeat=repeat, subrepeat=False)


class PicaPlainItem(PicaPlain):

    def __init__(self, plain):
        super().__init__(plain)


class PicaPlainLocal(PicaPlain):

    def __init__(self, plain, item=PicaPlainItem):
        super().__init__(plain)
        self.item = item

    def get_iln(self):
        return self.get_subfield_unique("101@", "a")

    def _items_start(self):
        return [i for i, r in enumerate(self.rows) if r.find("201A") > -1]

    def _items_end(self):
        start_i = self._items_start()[1:]
        end_i = [i-1 for i in start_i]
        end_i.append(len(self.rows)-1)
        return end_i

    def get_items(self):
        start_i = self._items_start()
        end_i = self._items_end()
        if len(start_i) == len(end_i):
            items = []
            for j in range(len(start_i)):
                item = []
                for i in range(start_i[j], end_i[j]+1):
                    item.append(self.rows[i])
                items.append(item)
            if len(items) > 0:
                return items

    def parse_items(self):
        items = self.get_items()
        if items:
            return [self.item("\n".join(i)) for i in items]


class PicaPlainTitle(PicaPlain):

    def __init__(self, plain, local=PicaPlainLocal):
        super().__init__(plain)
        self.local = local

    def _local_start(self):
        return [i for i, r in enumerate(self.rows) if r.find("101@") > -1]

    def _local_end(self):
        start_i = self._local_start()[1:]
        end_i = [i-1 for i in start_i]
        end_i.append(len(self.rows)-1)
        return end_i

    def get_local(self):
        start_i = self._local_start()
        end_i = self._local_end()
        if len(start_i) == len(end_i):
            holdings = []
            for j in range(len(start_i)):
                holding = []
                for i in range(start_i[j], end_i[j]+1):
                    holding.append(self.rows[i])
                holdings.append(holding)
            if len(holdings) > 0:
                return holdings

    def parse_local(self):
        holdings = self.get_local()
        if holdings:
            return [self.local("\n".join(h)) for h in holdings]

    def get_items(self):
        holdings = self.parse_local()
        items = []
        for holding in holdings:
            holding_items = holding.get_items()
            if isinstance(holding_items, list):
                for i in holding_items:
                    items.append(i)
        if len(items) > 0:
            return items

    def parse_items(self):
        holdings = self.parse_local()
        items = []
        for holding in holdings:
            holding_items = holding.parse_items()
            if isinstance(holding_items, list):
                for i in holding_items:
                    items.append(i)
        if len(items) > 0:
            return items


class K10plusItem(PicaPlainItem):
    """
    https://format.k10plus.de/avram.pl?profile=k10plus-item
    """

    def __init__(self, plain):
        super().__init__(plain)

    def __repr__(self):
        return "{0} (EPN)".format(self.get_epn())

    def get_latest_transaction_date(self):
        return self.get_subfield_unique("201B", "0")

    def get_latest_transaction_time(self):
        return self.get_subfield_unique("201B", "t")

    def get_first_entry(self):
        return self.get_subfield_unique("201D", "0")

    def get_epn(self):
        return self.get_subfield_unique("203@", "0")

    def get_isil(self):
        return self.get_subfield_unique("209A", "B")

    def get_eln(self):
        first_entry = self.get_first_entry()
        if isinstance(first_entry, str):
            return first_entry.split(":")[0]

    def get_date_created(self):
        first_entry = self.get_first_entry()
        if isinstance(first_entry, str):
            first_entry_split = first_entry.split(":")
            if len(first_entry_split) > 1:
                return first_entry_split[1]

    def get_date_created_date(self):
        date_created = self.get_date_created()
        if isinstance(date_created, str):
            try:
                return datetime.datetime.strptime(date_created, "%d-%m-%y").date()
            except ValueError:  # xx-xx-xx
                pass

    def get_date_created_iso(self):
        date_created = self.get_date_created_date()
        if isinstance(date_created, datetime.date):
            return date_created.isoformat()


class K10plusLocal(PicaPlainLocal):

    def __init__(self, plain):
        super().__init__(plain, item=K10plusItem)

    def __repr__(self):
        return "{0} (ILN)".format(self.get_iln())


class K10plusTitle(PicaPlainTitle):
    """
    https://format.k10plus.de/avram.pl?profile=k10plus-title
    """

    def __init__(self, plain):
        super().__init__(plain, local=K10plusLocal)

    def __repr__(self):
        return "{0} (PPN)".format(self.get_ppn())

    def get_first_entry(self):
        return self.get_subfield_unique("001A", "0")

    def get_latest_transaction_date(self):
        return self.get_subfield_unique("001B", "0")

    def get_latest_transaction_time(self):
        return self.get_subfield_unique("001B", "t")

    def get_ppn(self):
        return self.get_subfield_unique("003@", "0")

    def get_eln(self):
        first_entry = self.get_first_entry()
        if isinstance(first_entry, str):
            return first_entry.split(":")[0]

    def get_date_created(self):
        first_entry = self.get_first_entry()
        if isinstance(first_entry, str):
            first_entry_split = first_entry.split(":")
            if len(first_entry_split) > 1:
                return first_entry_split[1]

    def get_date_created_date(self):
        date_created = self.get_date_created()
        if isinstance(date_created, str):
            return datetime.datetime.strptime(date_created, "%d-%m-%y").date()

    def get_date_created_iso(self):
        date_created = self.get_date_created_date()
        if isinstance(date_created, datetime.date):
            return date_created.isoformat()

    def get_holding(self, epn):
        items = self.parse_items()
        if isinstance(items, list):
            for item in items:
                if item.get_epn() == epn:
                    return item

    def get_holdings_via_eln(self, eln):
        items = self.parse_items()
        if isinstance(items, list):
            items = [item for item in items if item.get_eln() == eln]
            return items if len(items) > 0 else None

    def get_holdings_via_iln(self, iln):
        locals = self.parse_local()
        if isinstance(locals, list):
            for local in locals:
                if local.get_iln() == iln:
                    return local.parse_items()

    def get_holdings_via_isil(self, isil):
        items = self.parse_items()
        if isinstance(items, list):
            items = [item for item in items if item.get_isil() == isil]
            return items if len(items) > 0 else None

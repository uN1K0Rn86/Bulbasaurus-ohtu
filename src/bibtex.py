from get_references import get_reference_info_by_id


class BibTex:
    def __init__(self, reference_id):
        self.reference_info = get_reference_info_by_id(reference_id)
        self.reference_type = self.reference_info["type"]
        self.reference_id = self.reference_info["id"]
        self.clean_reference_info_dictionary()

    def clean_reference_info_dictionary(self):
        """Make reference_info dictionary simpler by extractig only the values we need
        for the BibTex references, i.e. remove id and type."""
        new_dictionary = {}
        for bibtex_field, value in self.reference_info.items():
            if bibtex_field not in ("id", "type"):
                new_dictionary[bibtex_field] = value["field"]

        self.reference_info = new_dictionary

    def reference_in_bibtex_form(self) -> str:
        """Return the reference in BibTex form"""
        reference = self.reference_info
        reference_in_bibtex_form = ""
        reference_in_bibtex_form += self.first_line(self.reference_type)
        for value, field in reference.items():
            if field != "":
                if value == "author":
                    author = self.author_line(field)
                    reference_in_bibtex_form += author
                else:
                    line = self.normal_line(value, field)
                    reference_in_bibtex_form += line

        reference_in_bibtex_form += self.last_line()
        return reference_in_bibtex_form

    def first_line(self, reference_type):
        return "@" + reference_type + "{citekey,\n"

    def normal_line(self, value, field):
        return "    " + value + ' = "{' + field + '}",\n'

    def author_line(self, author):
        return "    author = {" + author + "},\n"

    def last_line(self):
        return "}"

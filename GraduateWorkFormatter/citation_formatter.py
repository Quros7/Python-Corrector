import re

class CitationFormatter:
    @staticmethod
    def format_helper(reference):
        """Formats a reference according to GOST standards.
        Returns:
            str: The formatted reference.
        """

        # Split the reference into parts
        parts = re.split(":", reference)
        formatted_reference = ""

        # Add the rest of the parts
        for part in parts[:len(parts)]:
            n_parts = re.split(",", part)
            for n_part in n_parts[:len(n_parts)-1]:
                formatted_reference += n_part.strip() + ", "
            formatted_reference += n_parts[-1].strip() + " : "

        formatted_reference = formatted_reference.removesuffix(' : ')
        if formatted_reference[-1] == "с":
            formatted_reference += "."

        return formatted_reference.strip()

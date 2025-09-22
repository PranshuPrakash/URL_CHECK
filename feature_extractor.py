# feature_extractor.py
import re
import tldextract
import pandas as pd

def feature_extractor(url: str) -> pd.DataFrame:
    """
    Extracts 94 features from a given URL and returns as a single-row DataFrame.
    """

    # ---- Basic counts ----
    qty_dot_url = url.count(".")
    qty_hyphen_url = url.count("-")
    qty_underline_url = url.count("_")
    qty_slash_url = url.count("/")
    qty_questionmark_url = url.count("?")
    qty_equal_url = url.count("=")
    qty_at_url = url.count("@")
    qty_and_url = url.count("&")
    qty_exclamation_url = url.count("!")
    qty_space_url = url.count(" ")
    qty_tilde_url = url.count("~")
    qty_comma_url = url.count(",")
    qty_plus_url = url.count("+")
    qty_asterisk_url = url.count("*")
    qty_hashtag_url = url.count("#")
    qty_dollar_url = url.count("$")
    qty_percent_url = url.count("%")
    qty_tld_url = 1 if "." in url.split("/")[-1] else 0
    length_url = len(url)

    # ---- Domain info ----
    extracted = tldextract.extract(url)
    domain = extracted.domain
    suffix = extracted.suffix
    subdomain = extracted.subdomain
    full_domain = ".".join(part for part in [subdomain, domain, suffix] if part)

    qty_dot_domain = full_domain.count(".")
    qty_hyphen_domain = full_domain.count("-")
    qty_underline_domain = full_domain.count("_")
    qty_slash_domain = full_domain.count("/")
    qty_questionmark_domain = full_domain.count("?")
    qty_equal_domain = full_domain.count("=")
    qty_at_domain = full_domain.count("@")
    qty_and_domain = full_domain.count("&")
    qty_exclamation_domain = full_domain.count("!")
    qty_space_domain = full_domain.count(" ")
    qty_tilde_domain = full_domain.count("~")
    qty_comma_domain = full_domain.count(",")
    qty_plus_domain = full_domain.count("+")
    qty_asterisk_domain = full_domain.count("*")
    qty_hashtag_domain = full_domain.count("#")
    qty_dollar_domain = full_domain.count("$")
    qty_percent_domain = full_domain.count("%")
    qty_vowels_domain = sum([full_domain.count(v) for v in "aeiou"])
    domain_length = len(full_domain)

    # ---- Directory (path) ----
    try:
        directory = re.findall(r"https?://[^/]+(/.*)", url)[0]
    except IndexError:
        directory = ""
    qty_dot_directory = directory.count(".")
    qty_hyphen_directory = directory.count("-")
    qty_underline_directory = directory.count("_")
    qty_slash_directory = directory.count("/")
    qty_questionmark_directory = directory.count("?")
    qty_equal_directory = directory.count("=")
    qty_at_directory = directory.count("@")
    qty_and_directory = directory.count("&")
    qty_exclamation_directory = directory.count("!")
    qty_space_directory = directory.count(" ")
    qty_tilde_directory = directory.count("~")
    qty_comma_directory = directory.count(",")
    qty_plus_directory = directory.count("+")
    qty_asterisk_directory = directory.count("*")
    qty_hashtag_directory = directory.count("#")
    qty_dollar_directory = directory.count("$")
    qty_percent_directory = directory.count("%")
    directory_length = len(directory)

    # ---- File ----
    file = url.split("/")[-1] if "." in url.split("/")[-1] else ""
    qty_dot_file = file.count(".")
    qty_hyphen_file = file.count("-")
    qty_underline_file = file.count("_")
    qty_slash_file = file.count("/")
    qty_questionmark_file = file.count("?")
    qty_equal_file = file.count("=")
    qty_at_file = file.count("@")
    qty_and_file = file.count("&")
    qty_exclamation_file = file.count("!")
    qty_space_file = file.count(" ")
    qty_tilde_file = file.count("~")
    qty_comma_file = file.count(",")
    qty_plus_file = file.count("+")
    qty_asterisk_file = file.count("*")
    qty_hashtag_file = file.count("#")
    qty_dollar_file = file.count("$")
    qty_percent_file = file.count("%")
    file_length = len(file)

    # ---- Params ----
    params = url.split("?")[1] if "?" in url else ""
    qty_dot_params = params.count(".")
    qty_hyphen_params = params.count("-")
    qty_underline_params = params.count("_")
    qty_slash_params = params.count("/")
    qty_questionmark_params = params.count("?")
    qty_equal_params = params.count("=")
    qty_at_params = params.count("@")
    qty_and_params = params.count("&")
    qty_exclamation_params = params.count("!")
    qty_space_params = params.count(" ")
    qty_tilde_params = params.count("~")
    qty_comma_params = params.count(",")
    qty_plus_params = params.count("+")
    qty_asterisk_params = params.count("*")
    qty_hashtag_params = params.count("#")
    qty_dollar_params = params.count("$")
    qty_percent_params = params.count("%")
    params_length = len(params)
    tld_present_params = 1 if any(suffix in params for suffix in [".com", ".net", ".org"]) else 0
    qty_params = params.count("&") + 1 if params else 0

    # ---- Collect everything ----
    features = {
        "qty_dot_url": qty_dot_url,
        "qty_hyphen_url": qty_hyphen_url,
        "qty_underline_url": qty_underline_url,
        "qty_slash_url": qty_slash_url,
        "qty_questionmark_url": qty_questionmark_url,
        "qty_equal_url": qty_equal_url,
        "qty_at_url": qty_at_url,
        "qty_and_url": qty_and_url,
        "qty_exclamation_url": qty_exclamation_url,
        "qty_space_url": qty_space_url,
        "qty_tilde_url": qty_tilde_url,
        "qty_comma_url": qty_comma_url,
        "qty_plus_url": qty_plus_url,
        "qty_asterisk_url": qty_asterisk_url,
        "qty_hashtag_url": qty_hashtag_url,
        "qty_dollar_url": qty_dollar_url,
        "qty_percent_url": qty_percent_url,
        "qty_tld_url": qty_tld_url,
        "length_url": length_url,
        "qty_dot_domain": qty_dot_domain,
        "qty_hyphen_domain": qty_hyphen_domain,
        "qty_underline_domain": qty_underline_domain,
        "qty_slash_domain": qty_slash_domain,
        "qty_questionmark_domain": qty_questionmark_domain,
        "qty_equal_domain": qty_equal_domain,
        "qty_at_domain": qty_at_domain,
        "qty_and_domain": qty_and_domain,
        "qty_exclamation_domain": qty_exclamation_domain,
        "qty_space_domain": qty_space_domain,
        "qty_tilde_domain": qty_tilde_domain,
        "qty_comma_domain": qty_comma_domain,
        "qty_plus_domain": qty_plus_domain,
        "qty_asterisk_domain": qty_asterisk_domain,
        "qty_hashtag_domain": qty_hashtag_domain,
        "qty_dollar_domain": qty_dollar_domain,
        "qty_percent_domain": qty_percent_domain,
        "qty_vowels_domain": qty_vowels_domain,
        "domain_length": domain_length,
        "qty_dot_directory": qty_dot_directory,
        "qty_hyphen_directory": qty_hyphen_directory,
        "qty_underline_directory": qty_underline_directory,
        "qty_slash_directory": qty_slash_directory,
        "qty_questionmark_directory": qty_questionmark_directory,
        "qty_equal_directory": qty_equal_directory,
        "qty_at_directory": qty_at_directory,
        "qty_and_directory": qty_and_directory,
        "qty_exclamation_directory": qty_exclamation_directory,
        "qty_space_directory": qty_space_directory,
        "qty_tilde_directory": qty_tilde_directory,
        "qty_comma_directory": qty_comma_directory,
        "qty_plus_directory": qty_plus_directory,
        "qty_asterisk_directory": qty_asterisk_directory,
        "qty_hashtag_directory": qty_hashtag_directory,
        "qty_dollar_directory": qty_dollar_directory,
        "qty_percent_directory": qty_percent_directory,
        "directory_length": directory_length,
        "qty_dot_file": qty_dot_file,
        "qty_hyphen_file": qty_hyphen_file,
        "qty_underline_file": qty_underline_file,
        "qty_slash_file": qty_slash_file,
        "qty_questionmark_file": qty_questionmark_file,
        "qty_equal_file": qty_equal_file,
        "qty_at_file": qty_at_file,
        "qty_and_file": qty_and_file,
        "qty_exclamation_file": qty_exclamation_file,
        "qty_space_file": qty_space_file,
        "qty_tilde_file": qty_tilde_file,
        "qty_comma_file": qty_comma_file,
        "qty_plus_file": qty_plus_file,
        "qty_asterisk_file": qty_asterisk_file,
        "qty_hashtag_file": qty_hashtag_file,
        "qty_dollar_file": qty_dollar_file,
        "qty_percent_file": qty_percent_file,
        "file_length": file_length,
        "qty_dot_params": qty_dot_params,
        "qty_hyphen_params": qty_hyphen_params,
        "qty_underline_params": qty_underline_params,
        "qty_slash_params": qty_slash_params,
        "qty_questionmark_params": qty_questionmark_params,
        "qty_equal_params": qty_equal_params,
        "qty_at_params": qty_at_params,
        "qty_and_params": qty_and_params,
        "qty_exclamation_params": qty_exclamation_params,
        "qty_space_params": qty_space_params,
        "qty_tilde_params": qty_tilde_params,
        "qty_comma_params": qty_comma_params,
        "qty_plus_params": qty_plus_params,
        "qty_asterisk_params": qty_asterisk_params,
        "qty_hashtag_params": qty_hashtag_params,
        "qty_dollar_params": qty_dollar_params,
        "qty_percent_params": qty_percent_params,
        "params_length": params_length,
        "tld_present_params": tld_present_params,
        "qty_params": qty_params,
    }

    return pd.DataFrame([features])

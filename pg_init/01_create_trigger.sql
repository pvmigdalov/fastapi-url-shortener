CREATE OR REPLACE FUNCTION generate_slug()
RETURNS TRIGGER AS $$
BEGIN
    NEW.slug := translate(
        encode(
            substring(decode(lpad(to_hex(NEW.id), 16, '0'), 'hex'), 1, 11),
            'base64'
        ),
        '+/', '-_'
    );
    NEW.slug := regexp_replace(NEW.slug, '=+$', '');
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER set_slug_trigger
BEFORE INSERT ON urls
FOR EACH ROW
WHEN (NEW.slug IS NULL OR NEW.slug = '')
EXECUTE FUNCTION generate_slug();
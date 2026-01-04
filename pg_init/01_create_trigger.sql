CREATE OR REPLACE FUNCTION generate_slug()
RETURNS TRIGGER AS $$
BEGIN
    NEW.slug := translate(
        encode(
            decode(to_hex(NEW.id), 'hex'),
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
WHEN (NEW.slug IS NULL)
EXECUTE FUNCTION generate_slug();
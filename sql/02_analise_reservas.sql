SELECT r.booking_id, h.hotel_name, c.name AS customer_name, r.check_in_date
FROM reservations r
INNER JOIN hotels h ON r.hotel_id = h.hotel_id
INNER JOIN customers c ON r.customer_id = c.customer_id;

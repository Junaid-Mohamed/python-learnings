print('Hi World')

def bolo(n):
    print(n)

bolo("Kaise hain?")

'''
Q7

SELECT COUNT(*) AS orders_with_more_than_two_items
FROM (
    SELECT order_id
    FROM public.order_details
    GROUP BY order_id
    HAVING COUNT(*) > 2
) AS sub;

'''


'''
Q8
select extract(month from order_date) as month from public.orders
where payment_method in ('Credit Card','Debit Card')
group by month
order by count(*) Desc
limit 1
'''

"""
Q9.
SELECT 
    o.payment_method,
    COUNT(od.id) AS count
FROM 
    public.orders o
JOIN 
    public.order_details od 
    ON o.order_id = od.order_id
GROUP BY 
    o.payment_method
# ORDER BY 
# count DESC;
"""

"""
q10.
SELECT COUNT(DISTINCT od.order_id) AS count
FROM public.order_details od
JOIN public.product_detail pd
  ON od.product_id = pd.product_id
WHERE pd.product_name = 'Avocado Salad';
"""

"""
q.11
SELECT 
    payment_method,
    ROUND(COUNT(order_id) / COUNT(DISTINCT customer_id), 1) AS ratio
FROM 
    public.orders
GROUP BY 
    payment_method;
    """

"""q12
SELECT 
    'Green Leaf Lettuce' AS product_name,
    COUNT(DISTINCT CASE WHEN o.status = 'processed' THEN o.order_id END) AS processed_orders,
    COUNT(DISTINCT CASE WHEN o.status = 'pending' THEN o.order_id END) AS pending_orders,
    COUNT(DISTINCT CASE WHEN o.status = 'shipped' THEN o.order_id END) AS shipped_orders,
    COUNT(DISTINCT CASE WHEN o.status = 'cancelled' THEN o.order_id END) AS cancelled_orders
FROM 
    public.orders o
JOIN 
    public.order_details od ON o.order_id = od.order_id
JOIN 
    public.product_detail pd ON od.product_id = pd.product_id
WHERE 
    pd.product_name = 'Green Leaf Lettuce';

"""

"""
q13
SELECT 
    o.order_id
FROM 
    public.order_details od
JOIN 
    public.product_detail pd ON od.product_id = pd.product_id
JOIN 
    public.orders o ON od.order_id = o.order_id
GROUP BY 
    o.order_id
ORDER BY 
    SUM(pd.weight) DESC
LIMIT 3;

"""

"""
q14.
SELECT 
    processed.payment_method,
    CONCAT(ROUND((COALESCE(shipped.count, 0) * 100.0) / processed.count, 2), '%') AS concat
FROM 
    (
        SELECT payment_method, COUNT(*) AS count
        FROM public.orders
        WHERE status = 'processed'
        GROUP BY payment_method
    ) AS processed
LEFT JOIN 
    (
        SELECT payment_method, COUNT(*) AS count
        FROM public.orders
        WHERE status = 'shipped'
        GROUP BY payment_method
    ) AS shipped
ON processed.payment_method = shipped.payment_method;

"""

'''
q15
SELECT 
    curr.year,
    ROUND(((curr.gdp - prev.gdp) / prev.gdp) * 100, 2) || '%' AS yoy
FROM 
    public.usa_gdp curr
JOIN 
    public.usa_gdp prev
    ON curr.year = prev.year + 1
WHERE 
    curr.year BETWEEN 1970 AND 1980
ORDER BY 
    curr.year;
'''


'''
q16
SELECT 
    pd.product_name
FROM 
    public.order_details od
JOIN 
    public.orders o ON od.order_id = o.order_id
JOIN 
    public.product_detail pd ON od.product_id = pd.product_id
WHERE 
    EXTRACT(YEAR FROM o.order_date) = 2021
GROUP BY 
    pd.product_name
HAVING 
    COUNT(DISTINCT EXTRACT(MONTH FROM o.order_date)) > 6;
'''


''''
q17
din't understand this
SELECT customer_id
FROM (
    SELECT customer_id,
           ROW_NUMBER() OVER (ORDER BY order_date DESC) AS rn
    FROM public.orders
    WHERE order_date >= '2020-07-01' AND order_date < '2020-08-01'
) sub
WHERE rn = 2;

'''

'''
q18
din't understand this..

SELECT COUNT(CASE WHEN born < last_pres_born_date THEN 1 ELSE NULL END) AS COUNT
FROM (
  SELECT *, LAG(born) OVER(ORDER BY position) AS last_pres_born_date
  FROM public.usa_presidents
) AS XY;

'''

'''
q19
this also not understood

WITH occupation_stats AS (
    SELECT 
        occupation,
        COUNT(*) AS occ_count,
        SUM(years_in_office) AS total_years
    FROM public.usa_presidents
    GROUP BY occupation
),
ranked_occupations AS (
    SELECT *,
           RANK() OVER (ORDER BY occ_count DESC, total_years DESC) AS occ_rank
    FROM occupation_stats
),
selected_occupation AS (
    SELECT occupation
    FROM ranked_occupations
    WHERE occ_rank = 2
),
filtered_presidents AS (
    SELECT *
    FROM public.usa_presidents
    WHERE occupation IN (SELECT occupation FROM selected_occupation)
    ORDER BY term_start
),
final_result AS (
    SELECT name
    FROM filtered_presidents
    LIMIT 1 OFFSET 2 -- get the third president (0-based indexing)
)
SELECT name FROM final_result;


'''

'''
q20.
hard din't understand.
WITH CTE_1 AS (
    SELECT *, 
           CASE 
               WHEN party <> LAG(party) OVER (ORDER BY position) THEN 1 
               ELSE 0 
           END AS new_streak
    FROM public.usa_presidents
    ORDER BY position
),
CTE_2 AS (
    SELECT *, 
           SUM(new_streak) OVER (ORDER BY position) AS streak_no
    FROM CTE_1
    ORDER BY position
),
CTE_3 AS (
    SELECT party, 
           streak_no, 
           COUNT(*) AS streak_count
    FROM CTE_2
    GROUP BY party, streak_no
)
SELECT position, name, term_start
FROM CTE_2
WHERE streak_no IN (
    SELECT streak_no 
    FROM CTE_3
    WHERE streak_count = (
        SELECT MAX(streak_count) 
        FROM CTE_3
    )
);

'''
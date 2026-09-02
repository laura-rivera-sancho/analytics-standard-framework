# Data Source Contract

| Key | Display name | Symbol | Measure | Transformation | Important limitation |
|---|---|---|---|---|---|
| `gold` | COMEX Gold Futures | `GC=F` | Daily close, USD per troy ounce | Log return | Futures are not the same as spot gold and may reflect contract mechanics. |
| `dxy` | U.S. Dollar Index | `DX-Y.NYB` | Daily index close | Log return | The index represents a fixed currency basket, not the Federal Reserve broad dollar index. |
| `us10y` | U.S. 10Y Yield | `^TNX` | Daily yield, percent | Percentage-point change | A yield index is not a constant-duration Treasury total-return series. |

**Provider:** Yahoo Finance public chart service.  
**Requested history:** five years, daily interval.  
**Refresh policy:** request-time retrieval with one-hour revalidation.  
**Join rule:** inner join on ISO trading date.  
**Null rule:** discard non-finite closes; never impute or forward-fill across calendars.  
**Failure behavior:** return a non-success status; the browser displays a deterministic, clearly labeled reference dataset.  
**Credentials:** none. No secrets or personal data are collected.

The provider is suitable for a public portfolio demonstration, not an institutional market-data entitlement. Production investment workflows should use a contracted source with service-level, adjustment, and redistribution terms.

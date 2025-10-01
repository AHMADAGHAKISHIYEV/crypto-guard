import { test, expect } from '@playwright/test';

test('homepage has disclaimer banner', async ({ page }) => {
  await page.goto('http://localhost:3000');
  await expect(page.locator('text=Yatırım tavsiyesi değildir')).toBeVisible();
});

import { Metadata } from '@zeedhi/core';
import { Select } from '@zeedhi/common';

export class SelectController {
  get selectedRestItemObject() {
    const selectObject = Metadata.getInstance<Select>('restSelectResult');
    const itemsText = (selectObject.value || '');
    return `selected value: ${JSON.stringify(itemsText)}`;
  }
}

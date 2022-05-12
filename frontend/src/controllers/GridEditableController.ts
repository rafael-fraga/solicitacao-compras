/* eslint-disable */
import { IEventParam } from '@zeedhi/core';
import { Button, GridEditable } from '@zeedhi/common';

export class GridEditableController {
  public isNotInlineCompsEditing = true;

  public onInlineEditComps({ component }: IEventParam<GridEditable>) {
    this.isNotInlineCompsEditing = !component.editing;
  }

  public async cancelEditingComps({ component }: IEventParam<Button>) {
    const grid = component.parent as GridEditable;
    await grid.cancelEditedRows();
    this.onInlineEditComps({ component: grid });
  }

  public async saveEditingComps({ component }: IEventParam<Button>) {
    const grid = component.parent as GridEditable;
    await grid.saveEditedRows();
    this.onInlineEditComps({ component: grid });
  }

  public teste() {
    console.log('Ttee');
  }
}

import { Text as teste } from '@zeedhi/common';
import { Metadata } from '@zeedhi/core';

export class RankingController {
  public xd() {
    const produto = Metadata.getInstance<teste>('text-item').text;
    return produto;
  }
}

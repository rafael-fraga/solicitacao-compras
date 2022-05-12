import { IComponentRender, ComponentRender } from '@zeedhi/common';

/**
 * JSON interface for ImgLink component
 */
export interface IImgLink extends IComponentRender {
  to?: string;
  src?: string;
}

export class ImgLink extends ComponentRender implements IImgLink {
  /**
   * Route path
   */
  public to: string = '';

  /**
   * Image source.
   */
  public src: string = '';

  /**
   * Creates a new instance of ImgLink
   * @param props Image Link props
   */
  constructor(props: IImgLink) {
    super(props);
    this.to = this.getInitValue('to', props.to, this.to);
    this.src = this.getInitValue('src', props.src, this.src);
    this.createAccessors();
  }
}
